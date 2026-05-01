from fastapi import FastAPI, APIRouter
from importlib import import_module
from pathlib import Path
from src.core.logging import get_logger

logger = get_logger(__name__)

def register_routers(app: FastAPI, base_path: str = "src.modules") -> None:
    modules_dir = Path(__file__).parent.parent / "modules"
    
    for module_dir in modules_dir.iterdir():
        if module_dir.is_dir() and not module_dir.name.startswith("_"):
            try:
                router_module = import_module(f"{base_path}.{module_dir.name}.router")
                if hasattr(router_module, "router"):
                    router = getattr(router_module, "router")
                    if isinstance(router, APIRouter):
                        prefix = f"/api/{app.api_version}/{module_dir.name}" if hasattr(app, "api_version") else f"/{module_dir.name}"
                        app.include_router(router, prefix=prefix)
                        logger.info(f"Registered router: {module_dir.name} at {prefix}")
            except (ImportError, AttributeError) as e:
                logger.debug(f"Could not load router from {module_dir.name}: {e}")
