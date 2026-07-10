from fastapi import APIRouter, HTTPException

from api.schemas.summary import SummarizeRequest, SummarizeResponse
from api.services.summary_service import run_summarize

router = APIRouter()

@router.post("", response_model=SummarizeResponse)
async def summarize(req: SummarizeRequest):
    try:
        return await run_summarize(req.uuid, req.text, req.ratio, req.engine)

    except HTTPException:
        raise  # 404 từ get_persona_row, giữ nguyên

    except TimeoutError as e:
        raise HTTPException(status_code=504, detail=str(e))

    except Exception as e:
        msg = str(e)
        if any(k in msg for k in ("API_KEY_INVALID", "PERMISSION_DENIED", "UNAUTHENTICATED", "401")):
            raise HTTPException(
                status_code=502,
                detail=f"Xác thực với model thất bại (kiểm tra GEMINI_API_KEY hoặc endpoint RunAI): {msg}",
            )
        if "RESOURCE_EXHAUSTED" in msg or "429" in msg or "rate" in msg.lower():
            raise HTTPException(status_code=429, detail=f"Model quota/rate limit: {msg}")
        raise HTTPException(status_code=502, detail=f"Lỗi khi sinh tóm tắt: {msg}")