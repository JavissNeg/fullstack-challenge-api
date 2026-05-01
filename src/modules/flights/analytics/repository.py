from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import Dict, List

from src.modules.flights.models import Aeropuerto, Aerolinea, Vuelo
from .exceptions import NoFlightDataFoundError


def _get_single_result(query, error_msg: str):
    result = query.first()
    if not result:
        raise NoFlightDataFoundError(error_msg)
    return result


def top_airport(db: Session) -> Dict:
    total = func.count(Vuelo.id_vuelo).label("total_movement")

    query = (
        db.query(
            Aeropuerto.nombre_aeropuerto.label("airport"),
            total
        )
        .join(Vuelo, Vuelo.id_aeropuerto == Aeropuerto.id_aeropuerto)
        .group_by(Aeropuerto.id_aeropuerto)
        .order_by(desc(total))
    )

    result = _get_single_result(query, "No airport data found")

    return {
        "airport": result.airport,
        "total_movement": result.total_movement
    }


def top_airline(db: Session) -> Dict:
    total = func.count(Vuelo.id_vuelo).label("total_flights")

    query = (
        db.query(
            Aerolinea.nombre_aerolinea.label("airline"),
            total
        )
        .join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea)
        .group_by(Aerolinea.id_aerolinea)
        .order_by(desc(total))
    )

    result = _get_single_result(query, "No airline data found")

    return {
        "airline": result.airline,
        "total_flights": result.total_flights
    }


def top_day(db: Session) -> Dict:
    day_expr = func.trim(func.to_char(Vuelo.dia, 'Day')).label("day")
    total = func.count(Vuelo.id_vuelo).label("total_flights")

    query = (
        db.query(day_expr, total)
        .group_by(day_expr)
        .order_by(desc(total))
    )

    result = _get_single_result(query, "No flight day data found")

    return {
        "day": result.day,
        "total_flights": result.total_flights
    }


def airlines_over_two_flights_per_day(db: Session) -> List[Dict]:
    total = func.count(Vuelo.id_vuelo).label("total")

    subquery = (
        db.query(
            Aerolinea.nombre_aerolinea.label("airline"),
            Vuelo.dia.label("day"),
            total
        )
        .join(Vuelo, Vuelo.id_aerolinea == Aerolinea.id_aerolinea)
        .group_by(Aerolinea.id_aerolinea, Vuelo.dia)
        .having(total > 2)
        .subquery()
    )

    query = (
        db.query(
            subquery.c.airline,
            func.count(subquery.c.day).label("days_with_over_two_flights")
        )
        .group_by(subquery.c.airline)
    )

    results = query.all()

    if not results:
        raise NoFlightDataFoundError(
            "No airlines found with more than two flights per day"
        )

    return [
        {
            "airline": r.airline,
            "days_with_over_two_flights": r.days_with_over_two_flights
        }
        for r in results
    ]