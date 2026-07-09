import asyncio

from fastapi import HTTPException
from fastapi.concurrency import run_in_threadpool

from pipeline.community import determine_community
from pipeline.worlds import build_worlds
from pipeline.prompt_builder import build_neutral_prompt
from pipeline.generation import generate_with_length_limit, generate_specific_with_length_limit

from pipeline import summarizer_gemini
from pipeline import summarizer_gpt

from api.dependencies import app_state, get_persona_row

STEP_TIMEOUT_SECONDS = 90  # mỗi bước (chung / riêng), đã bao gồm retry nội bộ

ENGINES = {
    "gemini": {
        "client_attr": "gemini_client",
        "retry_fn": summarizer_gemini.retry_generate,
        "summarize_fn": summarizer_gemini.summarize_person,
        "model_name": summarizer_gemini.SUMMARY_MODEL_NAME,
    },
    "gpt_oss": {
        "client_attr": "gpt_client",
        "retry_fn": summarizer_gpt.retry_generate,
        "summarize_fn": summarizer_gpt.summarize_person,
        "model_name": summarizer_gpt.SUMMARY_MODEL_NAME,
    },
}


async def _call_with_timeout(func, *args, timeout: float = STEP_TIMEOUT_SECONDS):
    try:
        return await asyncio.wait_for(run_in_threadpool(func, *args), timeout=timeout)
    except asyncio.TimeoutError:
        raise TimeoutError(f"Model không phản hồi sau {timeout}s (có thể do quota/kết nối).")


async def run_summarize(uuid: str, text: str, ratio: float = 0.7, engine: str = "gemini") -> dict:
    if engine not in ENGINES:
        raise ValueError(f"engine không hợp lệ: {engine} (chỉ chấp nhận 'gemini' hoặc 'gpt_oss')")

    cfg = ENGINES[engine]
    row = get_persona_row(uuid)
    client = getattr(app_state, cfg["client_attr"])

    if client is None:
        raise HTTPException(
            status_code=503,
            detail=f"Engine '{engine}' không khả dụng trên server này "
                   f"(thiếu cấu hình lúc khởi động — xem log server lúc startup).",
        )

    g = app_state.g

    community = determine_community(row)
    worlds = build_worlds(row)
    neutral_prompt = build_neutral_prompt(text)

    if engine == "gemini":
        generate_fn = client.models.generate_content
        base_kwargs = {"model": cfg["model_name"], "contents": neutral_prompt, "config": {"temperature": 0.0}}
    else:  # gpt_oss — generate_content_gpt không phải bound method, cần truyền client qua base_kwargs
        generate_fn = summarizer_gpt.generate_content_gpt
        base_kwargs = {"client": client, "model": cfg["model_name"], "contents": neutral_prompt,
                        "config": {"temperature": 0.0}}

    # Chung — khách quan
    general_summary, general_meta = await _call_with_timeout(
        generate_with_length_limit,
        generate_fn,
        cfg["retry_fn"],
        text,
        base_kwargs,
        "contents",
        ratio,
    )

    # Riêng — cá nhân hóa
    result, specific_meta = await _call_with_timeout(
        generate_specific_with_length_limit,
        cfg["summarize_fn"],
        cfg["retry_fn"],
        row, text, g, client,
        ratio,
    )

    return {
        "uuid": row.get("uuid", uuid),
        "engine": engine,
        "general_summary": general_summary,
        "specific_summary": result["summary"],
        "community": community,
        "worlds": worlds,
        "length_check": {"general": general_meta, "specific": specific_meta},
    }