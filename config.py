from pydantic_settings import BaseSettings, SettingsConfigDict
import json


class Settings(BaseSettings):
    BOT_TOKEN: str
    CHATS_CONFIG_PATH: str = "chats.json"
    ALBUM_DEBOUNCE_SECONDS: float = 0.7

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

with open(settings.CHATS_CONFIG_PATH, encoding="utf-8") as f:
    chats: dict[str, dict] = json.load(f)    