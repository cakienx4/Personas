import requests
import feedparser
import csv
import re
import time

CATEGORIES = {
    "thoi-su": "Thời sự",
    "the-gioi": "Thế giới",
    "kinh-doanh": "Kinh doanh",
    "phap-luat": "Pháp luật",
    "giao-duc": "Giáo dục",
    "khoa-hoc-cong-nghe": "Khoa học công nghệ",
    "suc-khoe": "Sức khỏe",
    "the-thao": "Thể thao",
    "giai-tri": "Giải trí",
    "du-lich": "Du lịch",
    "gia-dinh": "Đời sống",
    "bat-dong-san": "Bất động sản",
    "oto-xe-may": "Xe",
    "goc-nhin": "Góc nhìn",
}

BASE_URL = "https://vnexpress.net/rss/{}.rss"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def clean_summary(raw_html):
    text = re.sub(r"<a[^>]*>.*?</a>", "", raw_html, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def fetch_category(slug, category_name):
    url = BASE_URL.format(slug)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Lỗi khi lấy {slug}: {e}")
        return []

    feed = feedparser.parse(resp.content)
    rows = []
    for entry in feed.entries:
        rows.append({
            "category_slug": slug,
            "category_name": category_name,
            "title": entry.get("title", ""),
            "summary": clean_summary(entry.get("summary", "")),
        })
    return rows


def main():
    all_rows = []
    for slug, name in CATEGORIES.items():
        print(f"Đang lấy: {name} ({slug})")
        rows = fetch_category(slug, name)
        all_rows.extend(rows)
        time.sleep(0.5)

    print(f"Tổng cộng lấy được {len(all_rows)} bài")

    with open("vnexpress_rss_snapshot.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["category_slug", "category_name", "title", "summary"])
        writer.writeheader()
        writer.writerows(all_rows)


if __name__ == "__main__":
    main()