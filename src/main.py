from fastapi import FastAPI
from src.core.config import settings
from src.core.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    version=settings.api_version,
    description=settings.app_description,
    debug=settings.debug,
)

if __name__ == "__main__":
    logger.info(f"Starting {settings.app_name} {settings.api_version}")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level=settings.log_level.lower())

""" Helath route example """
@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok"}
