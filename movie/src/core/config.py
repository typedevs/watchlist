from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    RESET_TEST_DB: bool = True

    COLLECTION_NAME: str = 'movie'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
