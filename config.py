from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str

    CHAT_URL: str = "https://t.me/+URJp0_kZgahiN2Yy"
    BOOST_URL: str = "https://t.me/boost/aiogram_polygon"
    COMMENT_BANNER_FILE_ID: str = "AgACAgIAAxkBAAMFakIa9hToJHiZZZqX52gah5bKtZkAAosbaxs9jRBKo5gzScGUFgIBAAMCAAN4AAM8BA"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
