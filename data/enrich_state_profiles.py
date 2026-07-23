import json
import time
import csv
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
MODEL_NAME = "gemini-3.1-flash-lite"

client = genai.Client(api_key=API_KEY)
MAX_RETRY_ATTEMPTS = 5


def goi_llm(prompt):
    attempt = 0
    while True:
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={"temperature": 0.7},
            )
            return response.text.strip()
        except Exception as e:
            attempt += 1
            if attempt > MAX_RETRY_ATTEMPTS:
                raise RuntimeError(f"Loi sau {MAX_RETRY_ATTEMPTS} lan retry: {e}")
            print("Loi goi Gemini, thu lai lan", attempt, "->", e)
            time.sleep(10)


def tao_prompt_mo_ta(profile):
    prompt = f''' 
    Viết một đoạn mô tả persona bằng tiếng Việt, dài 3–4 câu, theo đúng phong cách sau:
Ví dụ phong cách cần theo:
- "Nhà phát triển phần mềm là những người đang tìm cách đơn giản hóa việc tích hợp công nghệ GPRS...
- "Một người quan tâm đến dinh dưỡng và sức khỏe..."
- "Lisa Bock, một chuyên gia dày dạn kinh nghiệm trong lĩnh vực bảo mật CNTT với hơn 20 năm kinh nghiệm..."
Quy tắc BẮT BUỘC:
- Bắt đầu bằng "Một [vai trò/chức danh]..." hoặc "Một người...", KHÔNG nhắc tên riêng.
- TUYỆT ĐỐI KHÔNG dùng đại từ nhân xưng như "tôi", "ông", "bà", "anh", "chị", "họ", "người này".
- Cấu trúc nội dung: vai trò/chức danh - mối quan tâm hoặc trách nhiệm chính - kiến thức chuyên môn hoặc kinh nghiệm liên quan - điều cần nắm bắt/tìm hiểu trong công việc hiện tại.
Thông tin để viết:
- Chức danh, tổ chức: {profile["mo_ta_chung"]}
- Ngành: {profile["nganh_to"]} - {profile["nganh_nho"]}
- Kinh nghiệm: {profile["kinh_nghiem"]}
- Mối quan tâm hiện tại: {profile["cau_hoi_truoc_mat"]}

Chỉ trả về đoạn mô tả, không đánh số câu, không giải thích gì thêm.
    '''
    return prompt


def tao_prompt_cau_hoi(profile):
    return f'''Mot can bo lam trong linh vuc {profile.get("nganh_nho", "")} thuoc nganh {profile.get("nganh_to", "")}, dang cong tac tai {profile.get("to_chuc", "")}. Hay viet 1 cau ve moi quan tam/cau hoi chinh sach ma nguoi nay dang can nam bat hien tai. Chi tra ve 1 cau, khong giai thich gi them.'''


def sinh_lai_bang_llm(danh_sach_profile):
    ket_qua = []
    for p in danh_sach_profile:
        try:
            p["cau_hoi_truoc_mat"] = goi_llm(tao_prompt_cau_hoi(p))
            p["mo_ta_chung"] = goi_llm(tao_prompt_mo_ta(p))
            print("Da xong profile:", p.get("id"))
        except Exception as e:
            print("Loi khi goi LLM cho profile", p.get("id"), "->", e)
        ket_qua.append(p)
        time.sleep(1)
    return ket_qua

def save_csv(profiles, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            "id", "mo_ta_chung", "nganh_to", "nganh_nho", "chu_de",
            "cau_hoi_truoc_mat", "to_chuc", "do_tuoi", "kinh_nghiem",
        ])
        for p in profiles:
            writer.writerow([
                p["id"], p["mo_ta_chung"], p["nganh_to"], p["nganh_nho"],
                " | ".join(p["chu_de"]), p["cau_hoi_truoc_mat"],
                p["to_chuc"], p["do_tuoi"], p["kinh_nghiem"],
            ])


if __name__ == "__main__":
    with open("state_profiles.json", "r", encoding="utf-8") as f:
        profiles = json.load(f)

    profiles_moi = sinh_lai_bang_llm(profiles)

    with open("state_profiles_enrich.json", "w", encoding="utf-8") as f:
        json.dump(profiles_moi, f, ensure_ascii=False, indent=2)

    save_csv(profiles_moi, "state_profiles_enrich.csv")

    print("Xong roi, da ghi de len state_profiles.json va state_profiles.csv")