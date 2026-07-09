# api/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gemini_api_key: str
    runai_endpoint: str = "https://text-sum-gpt-oss-120b-runai-text-sum.runai-inference.cyberspace.vn"
    class Config:
        env_file = ".env"

settings = Settings()