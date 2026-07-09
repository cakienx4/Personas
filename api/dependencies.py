import os
import sys
from pathlib import Path

import pandas as pd
from fastapi import HTTPException
from google import genai
from google.genai import types

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pipeline.ontology_context import load_graph

DATA_CSV = PROJECT_ROOT / "data" / "sample50.csv"
TTL_PATH = PROJECT_ROOT / "ontology" / "persona_analysis_3.ttl"   # khớp main.py


class AppState:
    def __init__(self):
        self.df: pd.DataFrame | None = None
        self.g = None
        self.client: genai.Client | None = None

    def load(self):
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            raise RuntimeError("Chưa set GEMINI_API_KEY (env hoặc .env)")
        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=60000),
        )
        self.df = pd.read_csv(DATA_CSV)
        self.g = load_graph(str(TTL_PATH))


app_state = AppState()


def get_persona_row(uuid: str) -> dict:
    match = app_state.df[app_state.df["uuid"] == uuid]
    if match.empty:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy uuid={uuid}")
    row = match.iloc[0]

    return {k: (v.item() if hasattr(v, "item") else v) for k, v in row.to_dict().items()}