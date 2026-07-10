# Personas — Hệ thống tóm tắt văn bản cá nhân hóa tiếng Việt

## Giới thiệu

Personas là hệ thống tóm tắt văn bản tiếng Việt được cá nhân hóa theo hồ sơ người dùng (persona),
dựa trên pipeline ontology-based. Với mỗi cặp (người dùng, văn bản), hệ thống sinh ra 2 loại tóm tắt:

- **Chung** — tóm tắt khách quan, trung lập, dùng làm baseline.
- **Riêng** — tóm tắt cá nhân hóa theo:
  - Lĩnh vực chuyên môn (Domain)
  - Kiểu bài viết (Type — tin tức, hướng dẫn, phỏng vấn...)
  - Loại bài viết (Genre — du lịch, ẩm thực, thể thao, nghệ thuật...)

**Dữ liệu gốc** lấy trên https://huggingface.co/datasets/nvidia/Nemotron-Personas-Vietnam

Cách lấy dữ liệu đầy đủ 100.000 rows: (nếu cần)

    from datasets import load_dataset
    
    # Personas tiếng Việt — Vietnamese personas
    nemotron_personas = load_dataset("nvidia/Nemotron-Personas-Vietnam", split="train") 


**Dữ liệu đầu vào cho project** là 50 hồ sơ dân sự trích từ dữ liệu gốc (`sample50.csv`),  dùng làm proof-of-concept cho phương pháp luận; ứng dụng thực tế nhắm tới các nhóm người dùng  chuyên biệt hơn (định hướng phát triển tiếp theo, ngoài phạm vi hiện tại).

## Kiến trúc pipeline

## Pipeline tổng quát

                         Hồ sơ người dùng (row)
                                  │
                                  ▼
                 Phân loại trường: HARD / SOFT / GENERAL
                                  │
                                  ▼
                           determine_community() ───────► 5 chiều cộng đồng
                                  │                     • Language
                                  │                     • Topic
                                  │                     • Domain
                                  │                     • Cultural
                                  │                     • Prototype
                                  │
                                  ▼
                           build_worlds()  ────────────► Hai thế giới
                                  │                     • Thế giới xác nhận (Factual World)
                                  │                     • Thế giới giả tưởng
                                  │                       - Bổn phận
                                  │                       - Mong muốn
                                  │                       - Niềm tin
                                  │
                                  ▼
                          classify_content() ─────────► Phân loại văn bản đầu vào
                                  │                     • Type (8 loại)
                                  │                     • Genre (11 loại)
                                  │
                                  ▼
                           build_prompt() ──────────► Ontology Context
                                  │                     + Community
                                  │                     + Worlds
                                  │                     + Văn bản đầu vào
                                  │                     ↓ Prompt cho LLM
                                  │
                                  ▼
                           summarize_person()───────────► LLM
                                  │                     • Gemini
                                  │                     • GPT-OSS-120B
                                  │
                                  ▼
                           Kết quả đầu ra
                            • Tóm tắt chung
                            • Tóm tắt cá nhân hóa


**Phân loại trường:**

| Loại | Các trường |
|---|---|
| HARD | age, education_level, occupation, country, skills_and_expertise, professional_persona |
| SOFT | sports_persona, arts_persona, travel_persona, culinary_persona, hobbies_and_interests, marital_status, zone |
| GENERAL | persona, cultural_background, career_goals_and_ambitions, region, sex |

## Cấu trúc thư mục
| Tên thư mục | Tên file |
|---|---|
|config  |      article_types.json, article_genres.json (định nghĩa Type/Genre + trọng số keyword)|
|data    |      sample50.csv, persona.csv, domain_keywords.json|
|pipeline |     mã nguồn chính (community.py, worlds.py, ontology_context.py, content_classifier.py, prompt_builder_2.py, summarizer.py, main.py...)|
|evaluation |   cq_validator_.py, ontology_score_.py, cq_test_cases.json, báo cáo .md/.json|
|ontology  |    persona_analysis_*.obo/.ttl/.html (10 branch, 574 terms, L0–L3)|
|document |     tài liệu thiết kế, định nghĩa CQ, hồ sơ mẫu|
|output |       profiles, inferences, summaries, summarization_guide (kết quả sinh ra) |


## Cài đặt

```bash
pip install -r requirements.txt
```

Cấu hình biến môi trường (API key Gemini, endpoint gpt-oss-120b nội bộ) — xem chi tiết trong
`pipeline/summarizer_gemini.py` và `pipeline/summarizer_gpt.py`.

## Sử dụng

```bash
# Chạy toàn bộ pipeline, sinh 5 file output cho mỗi cặp (person, text)
    1: nhập văn bản (chạy nhiều lần để thêm nhiều văn bản/chủ đề , kết thúc bằng một dòng chỉ chứa: END)
    python pipeline/input_text.py
    
    2: chạy pipeline, tự động xếp hạng và tóm tắt ưu tiên
    python pipeline/main.py --rows 2 5 15 --custom-texts
    
# Chạy main để test tóm tắt văn bản trong cq_test_case
    python pipeline/main.py --rows 2 5 15 --texts text_1 text_2
    python pipeline/main.py --all-rows --texts text_1
```
```bash
# Chạy validation Competency Question (CQ) — toàn bộ hoặc từng CQ riêng lẻ
python evaluation/cq_validator_gemini.py
python evaluation/cq_validator_gemini.py --cq CQ19

# Tính điểm ontology (feature coverage + CQ coverage)
python evaluation/ontology_score_gemini.py
```

## Đánh giá

- **CQ validation:** 20 câu hỏi năng lực (Competency Questions), đánh giá bằng LLM judge
  (Gemini và gpt-oss-120b, chạy song song để đối chiếu, `temperature=0.0` để đảm bảo tính
  determinstic của verdict).
- **Ontology score:** `(feature_coverage + CQ_coverage) / 2`, feature coverage tính qua 10 lệnh
  gọi LLM (1 lệnh/branch) đối chiếu với tên/synonym trong OBO.

## Giới hạn đã biết

- Bộ dữ liệu mẫu (`persona.csv`,`sample50.csv`, nguồn Nemotron-Personas-Vietnam) có xu hướng sinh nội dung tích cực cho mọi trường SOFT persona (ví dụ: không có hồ sơ nào có `arts_persona` thực sự "không quan tâm") — ảnh hưởng đến khả năng thiết kế test case tương phản nhị phân cao/thấp cho một số Competency Question. Đã xử lý bằng cơ chế chấm điểm cường độ (intensity scoring) thay vì kiểm tra nhị phân có/không.
- Một số CQ còn dao động verdict giữa các lần chạy do bản chất không hoàn toàn xác định của  LLM judge dù đã cố định `temperature=0.0`; các CQ này được ghi nhận và phân tích riêng thay  vì bị coi là lỗi pipeline.

## Ghi chú kỹ thuật
- SPARQL truy vấn ontology dùng `rdfs:subClassOf*` (transitive) để bao gồm cả term L2/L3.

## Chạy như REST API (FastAPI)

Ngoài chạy batch qua `pipeline/main.py` (Gemini) / `pipeline/main_gpt.py` (gpt-oss-120b),
dự án có thể chạy như REST API real-time qua tầng `api/` — dùng chung logic với
`pipeline/` (không duplicate code), hỗ trợ chọn model qua tham số `engine`.

### Cấu trúc tầng API

    api/
    ├── main.py                   # FastAPI app, khởi tạo lifespan
    ├── config.py                 # Settings (pydantic-settings) — đọc .env
    ├── dependencies.py           # AppState: load CSV, ontology graph, cả 2 client (Gemini + gpt-oss) 1 lần khi startup
    ├── engines.py                # Bảng cấu hình engine dùng chung (gemini / gpt_oss)
    ├── timeout_utils.py          # Wrapper timeout dùng chung cho mọi lệnh gọi LLM
    ├── schemas/                  # Pydantic request/response models
    │   ├── profile.py
    │   ├── inference.py
    │   ├── community.py
    │   ├── summary.py
    │   └── multi_summary.py
    ├── routers/                  # Định nghĩa endpoint
    │   ├── profiles.py
    │   ├── inferences.py
    │   ├── communities.py
    │   └── summarize.py          # gồm cả POST /summarize và POST /summarize/multi
    └── services/                 # Cầu nối router <-> pipeline, không chứa logic nghiệp vụ
    ├── profile_service.py
    ├── inference_service.py
    ├── community_service.py
    ├── summary_service.py
    └── multi_summary_service.py

### Cài đặt & chạy

1. `.env` ở root project:
2. Chạy server (từ root project):
```bash
uvicorn api.main:app --reload
```

3. Xem tài liệu API tự động tại: `http://localhost:8000/docs`

### Endpoint

| Method | Path                    | Mô tả                                                    | Gọi LLM? |
|--------|--------------------------|-------------------------------------------------------------|----------|
| GET    | `/profiles/{uuid}`       | Profile chuẩn hóa + community + worlds cho 1 person          | Không    |
| GET    | `/inferences/{uuid}`     | Chỉ 2 thế giới (xác nhận + giả tưởng)                        | Không    |
| GET    | `/communities/{uuid}`    | Chỉ community 5 chiều (Language/Topic/Domain/Cultural/Prototype) | Không |
| POST   | `/summarize`             | Sinh tóm tắt Chung + Riêng cho 1 cặp (uuid, text)            | Có       |
| POST   | `/summarize/multi`       | Sinh tóm tắt cho nhiều văn bản: Chung cho từng bài, Riêng đầy đủ cho bài phù hợp nhất, cực ngắn cho các bài còn lại | Có |

### Chọn model — tham số `engine`

Cả `/summarize` và `/summarize/multi` đều nhận tham số `engine`:
- `"gemini"` (mặc định) — `gemini-3.1-flash-lite`
- `"gpt_oss"` — `gpt-oss-120b` qua endpoint RunAI nội bộ

Nếu server thiếu cấu hình cho engine được chọn (thiếu `GEMINI_API_KEY`, hoặc endpoint RunAI không khởi tạo được), API trả lỗi `503` rõ ràng thay vì crash.

### Ví dụ request `/summarize`

```json
{
  "uuid": "b4a879dc2a074fec9a83ed171d1a0bc9",
  "text": "Nội dung văn bản cần tóm tắt...",
  "ratio": 0.7,
  "engine": "gemini"
}
```

### Ví dụ request `/summarize/multi`

```json
{
  "uuid": "b4a879dc2a074fec9a83ed171d1a0bc9",
  "texts": {
    "text_1": "Nội dung văn bản 1...",
    "text_2": "Nội dung văn bản 2..."
  },
  "ratio": 0.7,
  "engine": "gemini"
}
```
Tối đa 8 văn bản/request — endpoint gọi LLM tuần tự (N lần Chung + 1 lần Riêng + (N-1) lần cực ngắn), nên số văn bản lớn sẽ kéo dài thời gian phản hồi tương ứng.

### Khác biệt so với `pipeline/main.py` / `main_gpt.py` (CLI)

- CLI chạy batch, ghi 5 loại file output/(person, text) vào `output/`.
- API chạy real-time từng request, trả JSON trực tiếp, **không ghi file**.
- Cả CLI và API dùng chung `pipeline/community.py`, `pipeline/worlds.py`,
  `pipeline/generation.py`, `pipeline/summarizer_gemini.py`, `pipeline/summarizer_gpt.py`
  — không duplicate logic nghiệp vụ giữa 2 model hay giữa CLI/API.