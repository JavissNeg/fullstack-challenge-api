from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import datetime
from src.core.database import get_db
from .schemas import HealthStatus

router = APIRouter()

@router.get(
    "/",
    response_model=HealthStatus,
    summary="Verificación de estado del servicio",
    description="Verifica el estado general del servicio y conectividad con la base de datos.",
    response_description="Estado actual del servicio"
)
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
        status = "healthy"
    except Exception as e:
        db_status = f"error: {str(e)}"
        status = "unhealthy"

    return HealthStatus(
        status=status,
        database=db_status,
        timestamp=datetime.utcnow().isoformat() + "Z"
    )
