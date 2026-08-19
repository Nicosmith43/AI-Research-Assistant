from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "AI Research Assistant"
    ENVIRONMENT: str = "development"
    OPENAI_API_KEY: str = ""

    # Comma-separated list of allowed frontend origins, e.g.
    # "http://localhost:5173,https://your-frontend.vercel.app"
    CORS_ORIGINS_RAW: str = "http://localhost:5173,http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def CORS_ORIGINS(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.CORS_ORIGINS_RAW.split(",")
            if origin.strip()
        ]


settings = Settings()