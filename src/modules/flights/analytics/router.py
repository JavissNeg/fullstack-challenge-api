from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from .schemas import AirportStats, AirlineStats, DayStats, AirlineOverTwo
from src.modules.flights.analytics.service import (
    get_top_airport,
    get_top_airline,
    get_top_day,
    get_airlines_over_two
)

router = APIRouter()

@router.get(
    "/top-airport",
    response_model=AirportStats,
    summary="Aeropuerto con más movimientos",
    description="Obtiene el aeropuerto con mayor número de movimientos de vuelo.",
    response_description="Aeropuerto más activo"
)
def analytics_top_airport(db: Session = Depends(get_db)):
    return get_top_airport(db)

@router.get(
    "/top-airline",
    response_model=AirlineStats,
    summary="Aerolínea con más vuelos",
    description="Obtiene la aerolínea con mayor número de vuelos registrados.",
    response_description="Aerolínea más activa"
)
def analytics_top_airline(db: Session = Depends(get_db)):
    return get_top_airline(db)

@router.get(
    "/top-day",
    response_model=DayStats,
    summary="Día más concurrido",
    description="Obtiene el día de la semana con mayor actividad de vuelos.",
    response_description="Día con más vuelos"
)
def analytics_top_day(db: Session = Depends(get_db)):
    return get_top_day(db)

@router.get(
    "/airlines-over-two",
    response_model=list[AirlineOverTwo],
    summary="Aerolíneas con >2 vuelos diarios",
    description="Obtiene aerolíneas que operan más de 2 vuelos en un día.",
    response_description="Aerolíneas de alta frecuencia"
)
def analytics_airlines_over_two(db: Session = Depends(get_db)):
    return get_airlines_over_two(db)
