from pydantic import BaseModel, Field
from typing import List

class AirportStats(BaseModel):
    """
    Estadísticas de aeropuerto.
    """
    airport: str = Field(
        ...,
        description="Nombre del aeropuerto",
        examples=["Aeropuerto Internacional Benito Juárez"]
    )
    total_movement: int = Field(
        ...,
        description="Número total de movimientos de vuelo (llegadas + salidas)",
        examples=[1250]
    )

    class Config:
        schema_extra = {
            "example": {
                "airport": "Aeropuerto Internacional Benito Juárez",
                "total_movement": 1250
            }
        }

class AirlineStats(BaseModel):
    """
    Estadísticas de aerolínea.
    """
    airline: str = Field(
        ...,
        description="Nombre de la aerolínea",
        examples=["Aeroméxico"]
    )
    total_flights: int = Field(
        ...,
        description="Número total de vuelos operados por la aerolínea",
        examples=[450]
    )

    class Config:
        schema_extra = {
            "example": {
                "airline": "Aeroméxico",
                "total_flights": 450
            }
        }

class DayStats(BaseModel):
    """
    Estadísticas por día de la semana.
    """
    day: str = Field(
        ...,
        description="Día de la semana",
        examples=["Lunes", "Martes"]
    )
    total_flights: int = Field(
        ...,
        description="Número total de vuelos en este día",
        examples=[320]
    )

    class Config:
        schema_extra = {
            "example": {
                "day": "Lunes",
                "total_flights": 320
            }
        }

class AirlineOverTwo(BaseModel):
    """
    Aerolíneas con más de 2 vuelos diarios.
    """
    airline: str = Field(
        ...,
        description="Nombre de la aerolínea",
        examples=["Aeroméxico"]
    )
    days_with_over_two_flights: int = Field(
        ...,
        description="Número de días donde la aerolínea tuvo más de 2 vuelos",
        examples=[15]
    )

    class Config:
        schema_extra = {
            "example": {
                "airline": "Aeroméxico",
                "days_with_over_two_flights": 15
            }
        }