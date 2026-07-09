"""
pipeline/summarizer_gpt.py

Module tóm tắt văn bản cá nhân hóa theo persona.
Bản dùng model gpt-oss-120b (OpenAI-compatible endpoint trên RunAI),
thay cho Gemini trong summarizer_gemini.py. Dùng chung cho pipeline
chính (main_gpt.py), evaluation (cq_validator_gpt.py), và API (api/).
"""

import re
import time
from types import SimpleNamespace

import httpx
from openai import OpenAI

from pipeline.community import determine_community
from pipeline.worlds import build_worlds
from pipeline.prompt_builder import build_prompt

# ── CẤU HÌNH MODEL  ─────────────────────────────
OSS_HOST   = "https://text-sum-gpt-oss-120b-runai-text-sum.runai-inference.cyberspace.vn"
MODEL_NAME = "gpt-oss-120b"
API_KEY    = "EMPTY"

SUMMARY_MODEL_NAME = MODEL_NAME

MAX_RETRY_ATTEMPTS = 5  # đồng bộ với summarizer_gemini.py — tránh retry vô hạn khi endpoint lỗi kéo dài


def get_client() -> OpenAI:
    """
    Khởi tạo OpenAI-compatible client trỏ tới endpoint gpt-oss-120b trên RunAI.
    Endpoint yêu cầu httpx.Client(verify=False) và timeout=180.
    """
    return OpenAI(
        api_key=API_KEY,
        base_url=f"{OSS_HOST}/v1",
        http_client=httpx.Client(verify=False),
        timeout=180,
    )


def retry_generate(func, *args, **kwargs):
    """
    Gọi lại hàm khi gặp lỗi tạm thời từ endpoint gpt-oss-120b (rate limit, quá tải).
    Giới hạn tối đa MAX_RETRY_ATTEMPTS lần — sau đó raise lỗi thay vì lặp vô hạn.
    """
    attempt = 0
    while True:
        try:
            return func(*args, **kwargs)

        except Exception as e:
            msg = str(e)
            attempt += 1

            if attempt > MAX_RETRY_ATTEMPTS:
                raise RuntimeError(
                    f"gpt-oss-120b vẫn lỗi sau {MAX_RETRY_ATTEMPTS} lần retry: {msg}"
                ) from e

            if any(k in msg for k in ("429", "rate", "RESOURCE_EXHAUSTED", "overloaded")):
                match = re.search(r"retry in ([0-9.]+)s", msg, re.IGNORECASE)
                wait = float(match.group(1)) + 2 if match else 35
                print(f"\nRate limit. Đợi {wait:.1f}s... (lần {attempt}/{MAX_RETRY_ATTEMPTS})")
                time.sleep(wait)
                continue

            raise


def summarize_person(row: dict, text: str, g, client: OpenAI,
                      model_name: str = SUMMARY_MODEL_NAME,
                      extra_instruction: str = "") -> dict:
    """
    Sinh tóm tắt cá nhân hóa cho một person (row) dựa trên văn bản đầu vào (text)
    và đồ thị ontology (g), dùng model gpt-oss-120b.
    """
    community = determine_community(row)
    worlds = build_worlds(row)
    prompt = build_prompt(row, text, g)
    if extra_instruction:
        prompt += f"\n\n[YÊU CẦU BỔ SUNG DO VI PHẠM ĐỘ DÀI]\n{extra_instruction}"

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=8192,
        extra_body={"reasoning_effort": "low"},
    )

    finish_reason = response.choices[0].finish_reason
    print(f"[DEBUG] finish_reason={finish_reason} | usage={response.usage}")

    raw_content = response.choices[0].message.content
    summary = raw_content.strip() if raw_content else ""

    return {
        "uuid": row.get("uuid", ""),
        "summary": summary,
        "community": community,
        "worlds": worlds,
        "prompt_len": len(prompt),
    }


def generate_content_gpt(client: OpenAI, model: str, contents: str, config: dict | None = None):
    """
    Adapter: mô phỏng interface response.text của Gemini (client.models.generate_content)
    bằng gpt-oss (client.chat.completions.create), để dùng chung được với
    pipeline/generation.py::generate_with_length_limit — hàm này gọi generate_fn(**kwargs)
    rồi đọc response.text, bất kể provider nào.

    Trước đây hàm này nằm trong main_gpt.py (chỉ CLI dùng được); chuyển sang đây để
    api/services/summary_service.py cũng import được mà không phải kéo theo argparse
    và các phần CLI-only khác của main_gpt.py.
    """
    temperature = (config or {}).get("temperature", 0.0)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": contents}],
        temperature=temperature,
        max_tokens=8192,
        extra_body={"reasoning_effort": "low"},
    )
    raw = response.choices[0].message.content
    return SimpleNamespace(text=raw.strip() if raw else "")
