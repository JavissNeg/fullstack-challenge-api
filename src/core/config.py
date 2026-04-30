from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Reto FullStack API"
    app_description: str = "API intermediaria para consumo de datos externos y SQL"
    api_version: str = "v1"
    debug: bool = True
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()