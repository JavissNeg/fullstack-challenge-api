from fastapi import FastAPI
from src.core.config import settings
from src.core.logging import get_logger
from src.core.handlers import app_exception_handler
from src.core.exceptions import AppException
from src.core.router_registry import register_routers
from src.core.swagger import configure_swagger_app
import os

logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description=settings.app_description,
    debug=settings.debug,
)

# Register global exception handlers
app.add_exception_handler(AppException, app_exception_handler)

# Configure Swagger/OpenAPI
configure_swagger_app(app)

app.api_version = settings.api_version
register_routers(app)

if __name__ == "__main__":
    logger.info(f"Starting {settings.app_name} {settings.api_version}")
    import uvicorn
    
    # Determinar si usar SSL basado en variables de entorno
    use_ssl = os.getenv("USE_SSL", "false").lower() == "true"
    ssl_keyfile = os.getenv("SSL_KEYFILE", settings.ssl_keyfile)
    ssl_certfile = os.getenv("SSL_CERTFILE", settings.ssl_certfile)
    port = int(os.getenv("SERVER_PORT", settings.server_port))
    
    # Determinar puerto automáticamente si se usa SSL
    if use_ssl and port == 8000:
        port = 8443
    
    uvicorn_kwargs = {
        "host": "0.0.0.0",
        "port": port,
        "log_level": settings.log_level.lower()
    }
    
    if use_ssl and os.path.exists(ssl_keyfile) and os.path.exists(ssl_certfile):
        logger.info(f"Starting with SSL on port {port}")
        uvicorn_kwargs.update({
            "ssl_keyfile": ssl_keyfile,
            "ssl_certfile": ssl_certfile
        })
    elif use_ssl:
        logger.warning(f"SSL requested but certificate files not found. Starting without SSL.")
    
    uvicorn.run(app, **uvicorn_kwargs)
