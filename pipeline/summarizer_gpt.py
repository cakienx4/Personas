"""
pipeline/summarizer_gpt.py

Module tóm tắt văn bản cá nhân hóa theo persona.
Bản dùng model gpt-oss-120b (OpenAI-compatible endpoint trên RunAI),
thay cho Gemini trong summarizer_gemini.py. Dùng chung cho pipeline
chính (main.py) và evaluation (cq_validator_gpt.py).
"""

import re
import time

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
    """
    while True:
        try:
            return func(*args, **kwargs)

        except Exception as e:
            msg = str(e)

            if any(k in msg for k in ("429", "rate", "RESOURCE_EXHAUSTED", "overloaded")):
                match = re.search(r"retry in ([0-9.]+)s", msg, re.IGNORECASE)
                wait = float(match.group(1)) + 2 if match else 35
                print(f"\nRate limit. Đợi {wait:.1f}s...")
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
