from datetime import date
from src.core.database import SessionLocal
from src.modules.flights.models import Aerolinea, Aeropuerto, Movimiento, Vuelo
from src.core.logging import get_logger

logger = get_logger(__name__)

AEROLINEAS_DATA = [
    {"id_aerolinea": 1, "nombre_aerolinea": "Volaris"},
    {"id_aerolinea": 2, "nombre_aerolinea": "Aeromar"},
    {"id_aerolinea": 3, "nombre_aerolinea": "Interjet"},
    {"id_aerolinea": 4, "nombre_aerolinea": "Aeromexico"},
]

AEROPUERTOS_DATA = [
    {"id_aeropuerto": 1, "nombre_aeropuerto": "Benito Juarez"},
    {"id_aeropuerto": 2, "nombre_aeropuerto": "Guanajuato"},
    {"id_aeropuerto": 3, "nombre_aeropuerto": "La paz"},
    {"id_aeropuerto": 4, "nombre_aeropuerto": "Oaxaca"},
]

MOVIMIENTOS_DATA = [
    {"id_movimiento": 1, "descripcion": "Salida"},
    {"id_movimiento": 2, "descripcion": "Llegada"},
]

VUELOS_DATA = [
    # Aerolínea 1 
    {"id_aerolinea": 1, "id_aeropuerto": 1, "id_movimiento": 1, "dia": date(2021, 5, 2)},
    {"id_aerolinea": 1, "id_aeropuerto": 2, "id_movimiento": 1, "dia": date(2021, 5, 2)},
    {"id_aerolinea": 1, "id_aeropuerto": 3, "id_movimiento": 1, "dia": date(2021, 5, 2)},

    # Aerolínea 2
    {"id_aerolinea": 2, "id_aeropuerto": 1, "id_movimiento": 1, "dia": date(2021, 5, 2)},
    {"id_aerolinea": 2, "id_aeropuerto": 3, "id_movimiento": 1, "dia": date(2021, 5, 2)},

    # Aerolínea 3 
    {"id_aerolinea": 3, "id_aeropuerto": 2, "id_movimiento": 2, "dia": date(2021, 5, 2)},
    {"id_aerolinea": 3, "id_aeropuerto": 4, "id_movimiento": 1, "dia": date(2021, 5, 4)},
    {"id_aerolinea": 3, "id_aeropuerto": 4, "id_movimiento": 1, "dia": date(2021, 5, 4)},

    # Aerolínea 4 
    {"id_aerolinea": 4, "id_aeropuerto": 3, "id_movimiento": 2, "dia": date(2021, 5, 2)},
    {"id_aerolinea": 4, "id_aeropuerto": 3, "id_movimiento": 2, "dia": date(2021, 5, 2)},
]

if __name__ == "__main__":
    db = SessionLocal()
    try:
        db.bulk_insert_mappings(Aerolinea, AEROLINEAS_DATA)
        db.bulk_insert_mappings(Aeropuerto, AEROPUERTOS_DATA)
        db.bulk_insert_mappings(Movimiento, MOVIMIENTOS_DATA)
        db.bulk_insert_mappings(Vuelo, VUELOS_DATA)

        db.commit()
        logger.info("Seed completed successfully")
    except Exception:
        logger.exception("Seed failed")
        db.rollback()
        raise
    finally:
        db.close()