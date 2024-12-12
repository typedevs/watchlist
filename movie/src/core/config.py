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

    @property
    def full_database_url(self):
        return (f"{self.DATABASE_URL}://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@"
                f"{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()