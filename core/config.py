from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "gcinside"

    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_CALLBACK_URL: str = os.getenv("GOOGLE_CALLBACK_URL")
    GOOGLE_AUTH_SCOPE: str = os.getenv("GOOGLE_AUTH_SCOPE")

    GITHUB_CLIENT_ID: str = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET: str = os.getenv("GITHUB_CLIENT_SECRET")
    GITHUB_CALLBACK_URL: str = os.getenv("GITHUB_CALLBACK_URL")
    GITHUB_AUTH_SCOPE: str = os.getenv("GITHUB_AUTH_SCOPE")

    ACCESS_TOKEN_EXPIRATION_TIME = int(os.getenv("ACCESS_TOKEN_EXPIRATION_TIME"))
    REFRESH_TOKEN_EXPIRATION_TIME = int(os.getenv("REFRESH_TOKEN_EXPIRATION_TIME"))
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


settings = Settings()
