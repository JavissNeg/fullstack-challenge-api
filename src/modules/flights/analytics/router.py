from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.modules.flights.analytics.service import (
    get_top_airport,
    get_top_airline,
    get_top_day,
    get_airlines_over_two
)

router = APIRouter(tags=["analytics"])

@router.get("/top-airport")
def analytics_top_airport(db: Session = Depends(get_db)):
    return get_top_airport(db)

@router.get("/top-airline")
def analytics_top_airline(db: Session = Depends(get_db)):
    return get_top_airline(db)

@router.get("/top-day")
def analytics_top_day(db: Session = Depends(get_db)):
    return get_top_day(db)

@router.get("/airlines-over-two")
def analytics_airlines_over_two(db: Session = Depends(get_db)):
    return get_airlines_over_two(db)
