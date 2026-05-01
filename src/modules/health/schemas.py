from pydantic import BaseModel, Field
from datetime import datetime

class HealthStatus(BaseModel):
    """
    Estado de verificación de salud del servicio.
    """
    status: str = Field(
        ...,
        description="Estado general del servicio",
        examples=["healthy", "unhealthy"]
    )
    database: str = Field(
        ...,
        description="Estado de conexión a la base de datos",
        examples=["connected", "error: connection failed"]
    )
    timestamp: str = Field(
        ...,
        description="Timestamp de verificación de estado en formato ISO",
        examples=["2024-01-15T10:30:00Z"]
    )

    class Config:
        schema_extra = {
            "example": {
                "status": "healthy",
                "database": "connected",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }