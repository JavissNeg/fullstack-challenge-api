import logging
from src.core.config import settings

logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)