from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'Hello FastAPI'


settings = Settings()
