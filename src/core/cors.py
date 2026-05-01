
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.core.logging import get_logger

logger = get_logger(__name__)


def configure_cors(app):
    origins = [origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()]
    methods = [method.strip() for method in settings.cors_methods.split(",")]
    headers = settings.cors_headers.split(",") if settings.cors_headers != "*" else ["*"]

    logger.info(f"CORS Origins: {origins}")
    logger.info(f"CORS Methods: {methods}")
    logger.info(f"CORS Headers: {headers}")
    logger.info(f"CORS Credentials: {settings.cors_credentials}")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=settings.cors_credentials,
        allow_methods=methods,
        allow_headers=headers if headers != ["*"] else "*",
    )