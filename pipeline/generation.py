"""
pipeline/generation.py

Các hàm sinh tóm tắt có kiểm soát độ dài (retry nếu vượt tỉ lệ cho phép).
Tách khỏi main.py để dùng chung giữa CLI (ghi file) và API (trả JSON) —
tránh duplicate logic ở hai nơi.
"""

from pipeline.summarizer_gemini import summarize_person, retry_generate


MAX_LENGTH_RETRIES = 2


def check_length(summary: str, source: str, ratio: float = 0.7) -> tuple[bool, int, int]:
    src_words = len(source.split())
    sum_words = len(summary.split())
    return sum_words <= ratio * src_words, sum_words, int(ratio * src_words)


def generate_with_length_limit(generate_fn, source_text: str, base_kwargs: dict,
                                 prompt_key: str, ratio: float = 0.7):
    """
    generate_fn: hàm gọi model, ví dụ client.models.generate_content
    base_kwargs: kwargs truyền vào generate_fn, PHẢI chứa prompt_key (vd "contents")
                 để hàm này sửa lại prompt ở các lần retry
    """
    attempt = 0
    feedback = ""
    last_summary = None
    last_count = None
    max_words = None

    while attempt <= MAX_LENGTH_RETRIES:
        kwargs = dict(base_kwargs)
        if feedback:
            kwargs[prompt_key] = kwargs[prompt_key] + f"\n\n[YÊU CẦU BỔ SUNG DO VI PHẠM ĐỘ DÀI]\n{feedback}"

        response = retry_generate(generate_fn, **kwargs)
        summary = response.text.strip() if hasattr(response, "text") else response["summary"].strip()

        ok, sum_words, max_words = check_length(summary, source_text, ratio)
        last_summary, last_count = summary, sum_words

        if ok:
            return summary, {"length_ok": True, "words": sum_words, "max_words": max_words, "attempts": attempt + 1}

        feedback = (f"Bản tóm tắt trước có {sum_words} từ, vượt quá giới hạn {max_words} từ "
                    f"(tối đa {int(ratio*100)}% số từ bản gốc). Hãy viết lại NGẮN HƠN, "
                    f"cắt bớt chi tiết phụ, không thêm câu mới.")
        attempt += 1

    return last_summary, {"length_ok": False, "words": last_count, "max_words": max_words, "attempts": attempt}


def generate_specific_with_length_limit(row, text, g, client, ratio: float = 0.7):
    attempt = 0
    feedback = ""
    result = None
    sum_words = None
    max_words = None

    while attempt <= MAX_LENGTH_RETRIES:
        result = retry_generate(summarize_person, row, text, g, client, extra_instruction=feedback)
        ok, sum_words, max_words = check_length(result["summary"], text, ratio)

        if ok:
            return result, {"length_ok": True, "words": sum_words, "max_words": max_words, "attempts": attempt + 1}

        feedback = (f"Bản tóm tắt trước có {sum_words} từ, vượt quá giới hạn {max_words} từ. "
                    f"Viết lại ngắn hơn, cắt chi tiết phụ, không thêm câu mới.")
        attempt += 1

    return result, {"length_ok": False, "words": sum_words, "max_words": max_words, "attempts": attempt}
