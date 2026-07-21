# -*- coding: utf-8 -*-
"""
generate_state_profiles.py
---------------------------
Sinh tập dữ liệu profile cho nhánh mở rộng của project Personas:
"Tóm tắt tin tức cá nhân hóa cho khối nhà nước / lực lượng vũ trang / ngoại giao".

Khác với sample50.csv (persona dân sự tổng quát, dịch từ Nemotron-Personas-Vietnam),
tập dữ liệu này được xây bằng taxonomy riêng, đặc thù khu vực công Việt Nam, KHÔNG
tái sử dụng sample50.

Cách sinh:
- Các trường categorical (ngành to, ngành nhỏ, tổ chức, độ tuổi, kinh nghiệm) -> rule-based,
  lấy mẫu ngẫu nhiên có kiểm soát phân bố (đều theo ngành to).
- Các trường văn bản tự nhiên (mo_ta_chung, cau_hoi_truoc_mat) -> template-based với nhiều
  biến thể câu / cụm từ được xáo trộn ngẫu nhiên, để tránh lặp lại y hệt giữa các dòng.
  (Có thể thay bằng lời gọi LLM thật — xem hàm `generate_text_with_llm()` ở cuối file,
  để trống làm điểm mở rộng khi tích hợp vào pipeline chính, dùng chung interface
  summarize_fn như trong pipeline/generation.py.)

Chạy:
    python generate_state_profiles.py --n 60 --seed 42 --out state_profiles

Output:
    state_profiles.csv
    state_profiles.json
"""

import argparse
import csv
import json
import random

# =========================================================================
# 1. TAXONOMY: 12 ngành to, mỗi ngành có ngành nhỏ, tổ chức, mapping chủ đề
# =========================================================================

TAXONOMY = {
    "Công chức hành chính nhà nước": {
        "nganh_nho": ["Nội vụ", "Cải cách hành chính", "Quản lý công vụ", "Thi đua - Khen thưởng"],
        "chu_de": ["Thời sự/Xã hội", "Chính trị/Pháp luật"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Nội vụ"),
            ("Tỉnh", "Sở", "Sở Nội vụ tỉnh {tinh}"),
            ("Xã", "UBND xã", "UBND xã {xa}, tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "cập nhật quy định mới về sắp xếp tổ chức bộ máy và tinh giản biên chế",
            "theo dõi tiến độ triển khai mô hình chính quyền địa phương 2 cấp",
            "nắm bắt hướng dẫn thi hành Luật Cán bộ, công chức sửa đổi",
            "cập nhật quy trình một cửa liên thông và chuyển đổi số thủ tục hành chính",
        ],
    },
    "Quân đội": {
        "nganh_nho": ["Lục quân", "Hải quân", "Không quân", "Hậu cần - Kỹ thuật", "Biên phòng"],
        "chu_de": ["Quốc phòng/An ninh", "Thời sự/Xã hội"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Quốc phòng"),
            ("Quân khu", "Bộ Tư lệnh", "Bộ Tư lệnh Quân khu {quankhu}"),
            ("Tỉnh", "Bộ Chỉ huy quân sự", "Bộ Chỉ huy Quân sự tỉnh {tinh}"),
            ("Đơn vị", "Lữ đoàn/Sư đoàn", "Lữ đoàn {so} đóng quân tại tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "theo dõi diễn biến hoạt động huấn luyện, diễn tập trên địa bàn phụ trách",
            "cập nhật chính sách hậu phương quân đội và chế độ đãi ngộ quân nhân",
            "nắm tình hình an ninh biên giới, chủ quyền biển đảo liên quan khu vực đóng quân",
            "cập nhật kế hoạch hợp tác quốc phòng song phương trong năm",
        ],
    },
    "Công an / Cảnh sát": {
        "nganh_nho": ["An ninh", "Cảnh sát điều tra", "Cảnh sát giao thông", "Phòng cháy chữa cháy", "Quản lý xuất nhập cảnh"],
        "chu_de": ["Quốc phòng/An ninh", "Chính trị/Pháp luật"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Công an"),
            ("Tỉnh", "Công an tỉnh", "Công an tỉnh {tinh}"),
            ("Xã", "Công an xã", "Công an xã {xa}, tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "theo dõi tình hình trật tự an toàn giao thông và tai nạn giao thông trên địa bàn",
            "cập nhật thủ đoạn tội phạm công nghệ cao, lừa đảo qua mạng để cảnh báo người dân",
            "nắm diễn biến an ninh trật tự dịp cao điểm, lễ hội trên địa bàn quản lý",
            "cập nhật quy định mới về xử phạt vi phạm hành chính trong lĩnh vực phụ trách",
        ],
    },
    "An ninh - Quốc phòng (hoạch định chính sách)": {
        "nganh_nho": ["Chiến lược quốc phòng", "Công nghiệp quốc phòng", "An ninh mạng quốc gia", "Đối ngoại quốc phòng"],
        "chu_de": ["Quốc phòng/An ninh", "Chính trị/Pháp luật"],
        "to_chuc": [
            ("Trung ương", "Cục/Vụ", "Cục Chiến lược - Bộ Quốc phòng"),
            ("Trung ương", "Học viện", "Học viện Quốc phòng"),
            ("Trung ương", "Ban Chỉ đạo", "Ban Chỉ đạo An ninh mạng quốc gia"),
        ],
        "cau_hoi_mau": [
            "theo dõi các báo cáo, phân tích tình hình an ninh khu vực và thế giới liên quan lĩnh vực phụ trách",
            "cập nhật chủ trương, chiến lược quốc phòng mới được ban hành",
            "nắm tiến độ các dự án hợp tác công nghiệp quốc phòng đang triển khai",
            "theo dõi diễn biến an ninh mạng, các sự cố tấn công mạng quy mô lớn gần đây",
        ],
    },
    "Ngoại giao": {
        "nganh_nho": ["Song phương", "Đa phương", "Lãnh sự", "Kinh tế đối ngoại", "Công tác người Việt Nam ở nước ngoài"],
        "chu_de": ["Ngoại giao/Quan hệ quốc tế", "Kinh tế/Tài chính"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Ngoại giao"),
            ("Nước ngoài", "Đại sứ quán", "Đại sứ quán Việt Nam tại {nuoc}"),
            ("Nước ngoài", "Tổng Lãnh sự quán", "Tổng Lãnh sự quán Việt Nam tại {nuoc}"),
            ("Tỉnh", "Sở Ngoại vụ", "Sở Ngoại vụ tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "cập nhật diễn biến quan hệ song phương với các đối tác chiến lược",
            "theo dõi lịch trình các hội nghị, diễn đàn đa phương sắp diễn ra",
            "nắm chính sách bảo hộ công dân và hỗ trợ cộng đồng người Việt ở nước ngoài",
            "cập nhật tình hình đàm phán các hiệp định thương mại, đầu tư song phương",
        ],
    },
    "Tài chính - Ngân sách": {
        "nganh_nho": ["Ngân sách nhà nước", "Thuế", "Hải quan", "Kho bạc Nhà nước", "Quản lý tài sản công"],
        "chu_de": ["Kinh tế/Tài chính", "Chính trị/Pháp luật"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Tài chính"),
            ("Tỉnh", "Sở", "Sở Tài chính tỉnh {tinh}"),
            ("Tỉnh", "Cục Thuế", "Cục Thuế tỉnh {tinh}"),
            ("Cửa khẩu", "Chi cục Hải quan", "Chi cục Hải quan cửa khẩu {cuakhau}"),
        ],
        "cau_hoi_mau": [
            "cập nhật quy định mới về định mức phân bổ ngân sách và chi thường xuyên",
            "theo dõi tiến độ giải ngân vốn đầu tư công của địa phương/đơn vị",
            "nắm chính sách thuế mới ban hành áp dụng cho doanh nghiệp và hộ kinh doanh",
            "cập nhật quy trình kê khai, quyết toán thuế điện tử",
        ],
    },
    "Ngân hàng - Tiền tệ": {
        "nganh_nho": ["Chính sách tiền tệ", "Giám sát ngân hàng", "Thanh toán", "Quản lý ngoại hối"],
        "chu_de": ["Kinh tế/Tài chính"],
        "to_chuc": [
            ("Trung ương", "Ngân hàng Nhà nước", "Ngân hàng Nhà nước Việt Nam"),
            ("Khu vực", "Chi nhánh NHNN", "Ngân hàng Nhà nước Chi nhánh Khu vực {khuvuc}"),
        ],
        "cau_hoi_mau": [
            "theo dõi diễn biến lãi suất điều hành và tác động đến thị trường tín dụng",
            "cập nhật biến động tỷ giá và chính sách quản lý ngoại hối",
            "nắm tình hình nợ xấu và các biện pháp giám sát an toàn hệ thống ngân hàng",
            "theo dõi lộ trình triển khai các quy định mới về thanh toán không dùng tiền mặt",
        ],
    },
    "Tư pháp - Pháp luật": {
        "nganh_nho": ["Xét xử", "Kiểm sát", "Thi hành án", "Xây dựng pháp luật", "Công chứng - Hộ tịch"],
        "chu_de": ["Chính trị/Pháp luật"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Tư pháp"),
            ("Tỉnh", "Tòa án nhân dân", "Tòa án nhân dân tỉnh {tinh}"),
            ("Tỉnh", "Viện kiểm sát nhân dân", "Viện kiểm sát nhân dân tỉnh {tinh}"),
            ("Tỉnh", "Sở Tư pháp", "Sở Tư pháp tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "cập nhật các luật, nghị định mới có hiệu lực liên quan lĩnh vực phụ trách",
            "theo dõi án lệ và các vụ việc điển hình được dư luận quan tâm",
            "nắm tiến độ thi hành án và các vướng mắc phát sinh trong thực tiễn",
            "cập nhật quy định mới về công chứng, hộ tịch điện tử",
        ],
    },
    "Y tế": {
        "nganh_nho": ["Khám chữa bệnh", "Y tế dự phòng", "Dược - Trang thiết bị y tế", "Bảo hiểm y tế"],
        "chu_de": ["Sức khỏe/Đời sống", "Thời sự/Xã hội"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Y tế"),
            ("Tỉnh", "Sở Y tế", "Sở Y tế tỉnh {tinh}"),
            ("Tỉnh", "Bệnh viện", "Bệnh viện Đa khoa tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "theo dõi diễn biến dịch bệnh theo mùa và khuyến cáo phòng chống",
            "cập nhật chính sách bảo hiểm y tế và mức hưởng mới",
            "nắm quy định mới về quản lý dược phẩm, trang thiết bị y tế",
            "theo dõi tình hình nhân lực và cơ sở vật chất y tế tuyến cơ sở",
        ],
    },
    "Giáo dục - Đào tạo": {
        "nganh_nho": ["Giáo dục phổ thông", "Giáo dục đại học", "Giáo dục nghề nghiệp", "Quản lý nhà giáo"],
        "chu_de": ["Giáo dục", "Thời sự/Xã hội"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Giáo dục và Đào tạo"),
            ("Tỉnh", "Sở GD&ĐT", "Sở Giáo dục và Đào tạo tỉnh {tinh}"),
            ("Trường", "Trường học", "Trường THPT {truong}, tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "cập nhật lịch thi, quy chế tuyển sinh và kỳ thi tốt nghiệp THPT",
            "theo dõi chính sách đổi mới chương trình giáo dục phổ thông",
            "nắm quy định mới về chế độ, chính sách đối với nhà giáo",
            "cập nhật thông tin tuyển sinh đại học, cao đẳng năm nay",
        ],
    },
    "Khoa học - Công nghệ - TT&TT": {
        "nganh_nho": ["Chuyển đổi số", "An toàn thông tin", "Viễn thông", "Nghiên cứu khoa học - Đổi mới sáng tạo"],
        "chu_de": ["Khoa học/Công nghệ"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Khoa học và Công nghệ"),
            ("Tỉnh", "Sở KH&CN", "Sở Khoa học và Công nghệ tỉnh {tinh}"),
            ("Tỉnh", "Sở TT&TT", "Sở Thông tin và Truyền thông tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "theo dõi tiến độ triển khai đề án chuyển đổi số của địa phương/đơn vị",
            "cập nhật cảnh báo về lỗ hổng bảo mật, sự cố an toàn thông tin",
            "nắm chính sách hỗ trợ doanh nghiệp khởi nghiệp đổi mới sáng tạo",
            "theo dõi xu hướng công nghệ mới (AI, dữ liệu lớn) áp dụng trong quản lý nhà nước",
        ],
    },
    "Nông nghiệp - Tài nguyên - Môi trường": {
        "nganh_nho": ["Nông nghiệp - Phát triển nông thôn", "Đất đai", "Môi trường", "Tài nguyên nước - Khí tượng"],
        "chu_de": ["Môi trường", "Kinh tế/Tài chính"],
        "to_chuc": [
            ("Trung ương", "Bộ", "Bộ Nông nghiệp và Môi trường"),
            ("Tỉnh", "Sở Nông nghiệp và Môi trường", "Sở Nông nghiệp và Môi trường tỉnh {tinh}"),
        ],
        "cau_hoi_mau": [
            "theo dõi diễn biến thiên tai, thời tiết cực đoan ảnh hưởng sản xuất nông nghiệp",
            "cập nhật quy định mới về quản lý, cấp phép sử dụng đất đai",
            "nắm tình hình xuất khẩu nông sản và các rào cản kỹ thuật thị trường",
            "theo dõi tiến độ xử lý các điểm nóng ô nhiễm môi trường trên địa bàn",
        ],
    },
}

TINH_LIST = ["Lạng Sơn", "Cao Bằng", "Thái Nguyên", "Tuyên Quang", "Phú Thọ","Lào Cai", "Lai Châu", "Điện Biên", "Sơn La","Hà Nội", "Hải Phòng", "Quảng Ninh", "Bắc Ninh", "Hưng Yên", "Ninh Bình","Huế", "Thanh Hóa", "Nghệ An", "Hà Tĩnh", "Quảng Trị","Đà Nẵng", "Quảng Ngãi", "Gia Lai", "Đắk Lắk", "Khánh Hòa", "Lâm Đồng","Thành phố Hồ Chí Minh", "Đồng Nai", "Tây Ninh","Cần Thơ", "Đồng Tháp", "Vĩnh Long", "An Giang", "Cà Mau"]

XA_LIST = ["Tân Hồng", "Vinh Hưng", "Hòa Trí", "Ô Lâm", "Tân Thành", "Bình Khê", "Đức Trọng", "Ea Ô", "Đá Bạc", "Sơn Tây", "Hoàng Văn Thụ", "Trùng Khánh", "Đồng Hỷ", "Sơn Dương", "Hạ Hòa", "Bảo Thắng", "Mường Nhé", "Tuần Giáo", "Mộc Châu", "Lạch Tray", "Hạ Long", "Đình Bảng", "Văn Lâm", "Phú Sơn", "Hương Thủy", "Quảng Xương", "Diễn Châu", "Cẩm Xuyên", "Gio Linh", "Hòa Vang", "Bình Sơn", "An Nhơn", "Bình Chánh", "Long Thành"]

NUOC_LIST = ["Nhật Bản", "Hàn Quốc", "Pháp", "Đức", "Úc", "Singapore", "Lào", "Campuchia"]
QUANKHU_LIST = ["1", "2", "3", "4", "5", "7", "9"]
KHUVUC_LIST = ["1", "3", "5", "7", "9", "11"]
CUAKHAU_LIST = ["Hữu Nghị", "Lào Cai", "Mộc Bài", "Cầu Treo", "Bờ Y"]
TRUONG_LIST = ["Chuyên Lê Hồng Phong", "Nguyễn Trãi", "Trần Phú", "Lý Thường Kiệt", "Phan Bội Châu"]

CAP_BAC_BY_KINHNGHIEM = [
    (1, 10, "Chuyên viên"),
    (10, 20, "Chuyên viên chính"),
    (20, 35, "Chuyên viên cao cấp / Lãnh đạo"),
]

MO_TA_TEMPLATES = [
    "{chuc_danh} tại {to_chuc}, {so_nam} năm công tác trong lĩnh vực {nganh_nho}, hiện phụ trách {mo_ta_cong_viec}.",
    "Công tác tại {to_chuc} với vai trò {chuc_danh}, có {so_nam} năm kinh nghiệm trong mảng {nganh_nho}; đang tập trung vào {mo_ta_cong_viec}.",
    "{chuc_danh} thuộc {to_chuc}, chuyên trách lĩnh vực {nganh_nho} với {so_nam} năm kinh nghiệm; công việc hiện tại xoay quanh {mo_ta_cong_viec}.",
]

CHUC_DANH_BY_CAPBAC = {
    "Chuyên viên": ["Chuyên viên", "Cán bộ", "Nhân viên nghiệp vụ"],
    "Chuyên viên chính": ["Chuyên viên chính", "Phó trưởng phòng", "Trưởng nhóm nghiệp vụ"],
    "Chuyên viên cao cấp / Lãnh đạo": ["Trưởng phòng", "Phó Giám đốc", "Chuyên viên cao cấp"],
}

MO_TA_CONG_VIEC_SUFFIX = [
    "tổng hợp báo cáo định kỳ và tham mưu chính sách",
    "theo dõi, đôn đốc thực hiện các nhiệm vụ được giao trên địa bàn",
    "xây dựng kế hoạch công tác và phối hợp liên ngành",
    "tiếp nhận, xử lý phản ánh và giải quyết công việc liên quan người dân/đơn vị",
]


def pick_to_chuc(nganh_to, rng):
    cap, loai, ten_template = rng.choice(TAXONOMY[nganh_to]["to_chuc"])
    ten = ten_template.format(
        tinh=rng.choice(TINH_LIST),
        xa=rng.choice(XA_LIST),
        nuoc=rng.choice(NUOC_LIST),
        quankhu=rng.choice(QUANKHU_LIST),
        khuvuc=rng.choice(KHUVUC_LIST),
        cuakhau=rng.choice(CUAKHAU_LIST),
        truong=rng.choice(TRUONG_LIST),
        so=rng.randint(1, 99),
    ) if "{" in ten_template else ten_template
    return {"cap": cap, "loai": loai, "ten": ten}


def pick_kinh_nghiem(rng):
    so_nam = rng.randint(1, 32)
    cap_bac = next(cb for lo, hi, cb in CAP_BAC_BY_KINHNGHIEM if lo <= so_nam < hi)
    if so_nam >= 20:
        cap_bac = CAP_BAC_BY_KINHNGHIEM[-1][2]
    return {"so_nam": so_nam, "cap_bac": cap_bac}


def pick_do_tuoi(so_nam, rng):
    # tuổi >= 22 (mới ra trường) + số năm công tác + nhiễu nhỏ
    return min(60, max(24, 22 + so_nam + rng.randint(0, 6)))


def build_profile(idx, nganh_to, rng):
    info = TAXONOMY[nganh_to]
    nganh_nho = rng.choice(info["nganh_nho"])
    to_chuc = pick_to_chuc(nganh_to, rng)
    kinh_nghiem = pick_kinh_nghiem(rng)
    do_tuoi = pick_do_tuoi(kinh_nghiem["so_nam"], rng)
    chuc_danh = rng.choice(CHUC_DANH_BY_CAPBAC[kinh_nghiem["cap_bac"]])
    mo_ta_cong_viec = rng.choice(MO_TA_CONG_VIEC_SUFFIX)
    mo_ta_template = rng.choice(MO_TA_TEMPLATES)

    mo_ta_chung = mo_ta_template.format(
        chuc_danh=chuc_danh,
        to_chuc=to_chuc["ten"],
        so_nam=kinh_nghiem["so_nam"],
        nganh_nho=nganh_nho,
        mo_ta_cong_viec=mo_ta_cong_viec,
    )

    cau_hoi_truoc_mat = rng.choice(info["cau_hoi_mau"]).capitalize() + "."

    return {
        "id": f"NN{idx:03d}",
        "mo_ta_chung": mo_ta_chung,
        "nganh_to": nganh_to,
        "nganh_nho": nganh_nho,
        "chu_de": info["chu_de"],
        "cau_hoi_truoc_mat": cau_hoi_truoc_mat,
        "to_chuc": to_chuc,
        "do_tuoi": do_tuoi,
        "kinh_nghiem": kinh_nghiem,
    }


def generate(n, seed):
    rng = random.Random(seed)
    nganh_list = list(TAXONOMY.keys())
    base = n // len(nganh_list)
    remainder = n % len(nganh_list)
    counts = {nganh: base for nganh in nganh_list}
    for nganh in rng.sample(nganh_list, remainder):
        counts[nganh] += 1

    profiles = []
    idx = 1
    for nganh_to, count in counts.items():
        for _ in range(count):
            profiles.append(build_profile(idx, nganh_to, rng))
            idx += 1
    rng.shuffle(profiles)
    # re-number after shuffle for clean sequential ids
    for i, p in enumerate(profiles, start=1):
        p["id"] = f"NN{i:03d}"
    return profiles


def save_csv(profiles, path):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            "id", "mo_ta_chung", "nganh_to", "nganh_nho", "chu_de",
            "cau_hoi_truoc_mat", "to_chuc_cap", "to_chuc_loai", "to_chuc_ten",
            "do_tuoi", "kinh_nghiem_so_nam", "kinh_nghiem_cap_bac",
        ])
        for p in profiles:
            writer.writerow([
                p["id"], p["mo_ta_chung"], p["nganh_to"], p["nganh_nho"],
                " | ".join(p["chu_de"]), p["cau_hoi_truoc_mat"],
                p["to_chuc"]["cap"], p["to_chuc"]["loai"], p["to_chuc"]["ten"],
                p["do_tuoi"], p["kinh_nghiem"]["so_nam"], p["kinh_nghiem"]["cap_bac"],
            ])


def save_json(profiles, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)


# =========================================================================
# Điểm mở rộng: thay template bằng LLM thật (dùng chung interface với
# pipeline/summarizer_gemini.py hoặc summarizer_gpt.py trong project chính)
# =========================================================================
def generate_text_with_llm(prompt, summarize_fn=None):
    """
    Placeholder cho việc sinh văn bản tự nhiên hơn bằng LLM thật.
    summarize_fn: hàm có signature giống summarize_person() trong project chính
                  (nhận prompt, trả về text). Để trống -> fallback dùng template.
    Khi tích hợp vào pipeline chính, có thể truyền vào từ generation.py để tái
    dùng logic retry/timeout đã có (check_length, generate_with_length_limit).
    """
    if summarize_fn is None:
        raise NotImplementedError(
            "Chưa cấu hình LLM backend trong sandbox này. "
            "Khi chạy trong project chính, truyền summarize_fn từ "
            "pipeline/summarizer_gemini.py hoặc summarizer_gpt.py vào đây."
        )
    return summarize_fn(prompt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sinh profile khối nhà nước/LLVT/ngoại giao")
    parser.add_argument("--n", type=int, default=60, help="Số lượng profile cần sinh")
    parser.add_argument("--seed", type=int, default=42, help="Seed để tái lập kết quả")
    parser.add_argument("--out", type=str, default="state_profiles", help="Tên file output (không đuôi)")
    args = parser.parse_args()

    profiles = generate(args.n, args.seed)
    save_csv(profiles, f"{args.out}.csv")
    save_json(profiles, f"{args.out}.json")
    print(f"Đã sinh {len(profiles)} profile -> {args.out}.csv / {args.out}.json")

    # thống kê nhanh để kiểm tra phân bố theo ngành to
    from collections import Counter
    dist = Counter(p["nganh_to"] for p in profiles)
    for k, v in dist.items():
        print(f"  {k}: {v}")