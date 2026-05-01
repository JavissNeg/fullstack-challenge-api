from fastapi.openapi.utils import get_openapi
from src.core.config import settings

def get_tag_for_path(path: str) -> str:
    """
    Determine the appropriate tag for a given API path.

    Args:
        path: The API path (e.g., "/api/v1/health/")

    Returns:
        The tag name for grouping endpoints
    """
    if "/health" in path:
        return "health"
    elif "/flights/analytics" in path:
        return "flights-analytics"
    elif "/stack/analytics" in path:
        return "stack-analytics"
    else:
        return "default"

def custom_openapi(app):
    """
    Custom OpenAPI schema generation with enhanced metadata and best practices.

    This function configures the OpenAPI schema with:
    - Detailed API metadata
    - Server configurations
    - Security schemes (if needed)
    - Organized tags
    - Contact and license information
    """

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.app_name,
        version=settings.api_version,
        description=settings.app_description,
        routes=app.routes,
        tags=[
            {
                "name": "health",
                "description": "Endpoints de verificación de estado del servicio"
            },
        ],
    )

    # Assign tags to operations based on their paths
    for path, methods in openapi_schema.get("paths", {}).items():
        for method, operation in methods.items():
            if "tags" not in operation or not operation["tags"]:
                tag = get_tag_for_path(path)
                operation["tags"] = [tag]

    # Add server configurations
    openapi_schema["servers"] = [
        {
            "url": "http://localhost:8000",
            "description": "Servidor de desarrollo"
        },
        {
            "url": "https://api.example.com",
            "description": "Servidor de producción"
        }
    ]

    # Security schemes disabled - add when authentication is implemented

    # Add global security requirement (commented out until authentication is implemented)
    # openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

def configure_swagger_app(app):
    """
    Configure FastAPI app with Swagger/OpenAPI settings.

    Args:
        app: FastAPI application instance
    """
    # Set custom OpenAPI schema generator
    app.openapi = lambda: custom_openapi(app)

    # Configure OpenAPI URLs
    app.docs_url = settings.docs_url
    app.redoc_url = settings.redoc_url
    app.openapi_url = settings.openapi_url

    return app