from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Reto FullStack API"
    app_description: str = """
        API intermediaria para consumo de datos externos y SQL. Proporciona endpoints para análisis de datos de vuelos, incluyendo estadísticas sobre aeropuertos, aerolíneas y días con más vuelos.
    """
    api_version: str = "v1"
    debug: bool = True
    log_level: str = "INFO"

    # Configuración Swagger/OpenAPI
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    # Información de Contacto
    contact_name: str = "Soporte API"
    contact_email: str = "soporte@example.com"

    # Licencia
    license_name: str = "MIT"
    license_url: str = "https://opensource.org/licenses/MIT"

    # Términos de Servicio
    terms_of_service: str = "https://example.com/terminos/"

    # Configuración de Base de Datos
    database_url: str
    database_echo: bool = False
    
    # Configuración de CORS
    cors_origins: str = "http://localhost:4200,https://localhost:4200"
    cors_credentials: bool = True
    cors_methods: str = "*"
    cors_headers: str = "*"


    # Configuración SSL/HTTPS
    use_ssl: bool = False
    ssl_keyfile: str = "certs/key.pem"
    ssl_certfile: str = "certs/cert.pem"
    server_port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()