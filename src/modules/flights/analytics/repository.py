from sqlalchemy.orm import Session
from sqlalchemy import func
from src.modules.flights.models import Aeropuerto, Aerolinea, Vuelo

def top_airport(db: Session):
    return db.query(
        Aeropuerto.nombre_aeropuerto,
        func.count(Vuelo.id_vuelo).label("total_movement")
    ).join(Vuelo).group_by(Aeropuerto.id_aeropuerto).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

def top_airline(db: Session):
    return db.query(
        Aerolinea.nombre_aerolinea,
        func.count(Vuelo.id_vuelo).label("total_flights")
    ).join(Vuelo).group_by(Aerolinea.id_aerolinea).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

def top_day(db: Session):
    return db.query(
        Vuelo.dia,
        func.count(Vuelo.id_vuelo).label("total_flights")
    ).group_by(Vuelo.dia).order_by(
        func.count(Vuelo.id_vuelo).desc()
    ).first()

def airlines_over_two_flights_per_day(db: Session):
    return db.query(
        Aerolinea.nombre_aerolinea,
        Vuelo.dia,
        func.count(Vuelo.id_vuelo).label("flights_per_day")
    ).join(Vuelo).group_by(
        Aerolinea.id_aerolinea, Vuelo.dia
    ).having(
        func.count(Vuelo.id_vuelo) > 2
    ).all()
