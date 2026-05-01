from sqlalchemy.orm import Session
from sqlalchemy import func
from src.modules.flights.models import Aeropuerto, Aerolinea, Vuelo
from .exceptions import NoFlightDataFoundError


def top_airport(db: Session):
    result = db.query(
        Aeropuerto.nombre_aeropuerto,
        func.count(Vuelo.id_vuelo).label("total_movement")
    ).join(Vuelo).group_by(Aeropuerto.id_aeropuerto).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

    if not result:
        raise NoFlightDataFoundError("No airport data found")

    return result


def top_airline(db: Session):
    result = db.query(
        Aerolinea.nombre_aerolinea,
        func.count(Vuelo.id_vuelo).label("total_flights")
    ).join(Vuelo).group_by(Aerolinea.id_aerolinea).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

    if not result:
        raise NoFlightDataFoundError("No airline data found")

    return result


def top_day(db: Session):
    result = db.query(
        func.to_char(Vuelo.dia, 'Day').label("day"),
        func.count(Vuelo.id_vuelo).label("total_flights")
    ).group_by(
        func.to_char(Vuelo.dia, 'Day')
    ).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

    if not result:
        raise NoFlightDataFoundError("No flight day data found")

    return {
        "day": result.day.strip(),
        "total_flights": result.total_flights
    }


def airlines_over_two_flights_per_day(db: Session):
    result = db.query(
        Aerolinea.nombre_aerolinea.label("airline"),
        Vuelo.dia.label("day"),
        func.count(Vuelo.id_vuelo).label("total")
    ).join(Vuelo).group_by(
        Aerolinea.id_aerolinea,
        Vuelo.dia
    ).having(
        func.count(Vuelo.id_vuelo) > 2
    ).all()

    if not result:
        raise NoFlightDataFoundError(
            "No airlines found with more than two flights per day"
        )

    # contar días por aerolínea
    stats = {}

    for r in result:
        stats[r.airline] = stats.get(r.airline, 0) + 1

    return [
        {
            "airline": airline,
            "days_with_over_two_flights": days
        }
        for airline, days in stats.items()
    ]