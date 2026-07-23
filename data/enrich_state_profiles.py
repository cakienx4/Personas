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
    return f'''Viet mot doan mo ta persona bang tieng Viet, dai 3-4 cau, theo dung cau truc sau:
- Cau 1: gioi thieu vai tro cua nguoi nay (chuc danh, noi cong tac).
- Cau 2: mo ta moi quan tam/trach nhiem chinh ho dang tap trung.
- Cau 3: the hien kien thuc chuyen mon hoac kinh nghiem lien quan linh vuc phu trach.
- Cau 4: dieu ho dang can nam bat/tim hieu trong cong viec hien tai.
Thong tin de viet:
- Chuc danh, to chuc: {profile.get("mo_ta_chung", "")}
- Nganh: {profile.get("nganh_to", "")}  -  {profile.get("nganh_nho", "")}
- Kinh nghiem: {profile.get("kinh_nghiem", "")}
- Moi quan tam hien tai: {profile.get("cau_hoi_truoc_mat", "")}
Chi tra ve doan mo ta, khong danh so cau, khong giai thich gi them.
'''


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

    with open("state_profiles.json", "w", encoding="utf-8") as f:
        json.dump(profiles_moi, f, ensure_ascii=False, indent=2)

    save_csv(profiles_moi, "state_profiles.csv")

    print("Xong roi, da ghi de len state_profiles.json va state_profiles.csv")