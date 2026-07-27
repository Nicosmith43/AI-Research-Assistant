from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Research Assistant"
    environment: str = "development"

    model_config = ConfigDict(
        env_file=".env"
    )


settings = Settings()