from sqlalchemy.orm import Session
from src.modules.flights.analytics.repository import (
    top_airport,
    top_airline,
    top_day,
    airlines_over_two_flights_per_day
)

def get_top_airport(db: Session):
    result = top_airport(db)
    return {
        "airport": result[0],
        "total_movement": result[1]
    } if result else None

def get_top_airline(db: Session):
    result = top_airline(db)
    return {
        "airline": result[0],
        "total_flights": result[1]
    } if result else None

def get_top_day(db: Session):
    result = top_day(db)
    return {
        "date": str(result[0]),
        "total_flights": result[1]
    } if result else None

def get_airlines_over_two(db: Session):
    results = airlines_over_two_flights_per_day(db)
    return [
        {
            "airline": r[0],
            "date": str(r[1]),
            "flights": r[2]
        }
        for r in results
    ]
