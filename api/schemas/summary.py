from typing import Any
from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    uuid: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1, description="Văn bản đầu vào cần tóm tắt")
    ratio: float = Field(0.7, gt=0, le=1, description="Tỉ lệ độ dài tối đa so với bản gốc")


class LengthMeta(BaseModel):
    length_ok: bool
    words: int
    max_words: int
    attempts: int


class SummarizeResponse(BaseModel):
    uuid: str
    general_summary: str
    specific_summary: str
    community: dict[str, Any]
    worlds: dict[str, Any]
    length_check: dict[str, LengthMeta]