from fastapi import FastAPI, APIRouter
from importlib import import_module
from pathlib import Path
from src.core.logging import get_logger
from src.core.config import settings

logger = get_logger(__name__)

def register_routers(app: FastAPI, base_path: str = "src.modules") -> None:
    base_dir = Path(__file__).resolve().parent.parent
    modules_dir = base_dir / "modules"

    for router_file in modules_dir.rglob("router.py"):
        try:
            relative_to_src = router_file.relative_to(base_dir.parent)  # src/...

            module_path = str(relative_to_src).replace("/", ".").replace(".py", "")

            router_module = import_module(module_path)

            if hasattr(router_module, "router"):
                router = getattr(router_module, "router")

                if isinstance(router, APIRouter):
                    parts = router_file.parts

                    idx = parts.index("modules")
                    route_parts = parts[idx + 1:-1]

                    prefix = f"/api/{settings.api_version}/" + "/".join(route_parts)

                    app.include_router(router, prefix=prefix)

                    logger.info(f"Registered router: {module_path} at {prefix}")

        except Exception as e:
            logger.error(f"Failed loading {router_file}: {e}")