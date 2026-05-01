from src.core.logging import get_logger
from .repository import (
    top_airport,
    top_airline,
    top_day,
    airlines_over_two_flights_per_day,
)

logger = get_logger(__name__)


def get_top_airport(db):
    result = top_airport(db)
    logger.info("Top airport computed")
    return result


def get_top_airline(db):
    result = top_airline(db)
    logger.info("Top airline computed")
    return result


def get_top_day(db):
    result = top_day(db)
    logger.info("Top day computed")
    return result


def get_airlines_over_two(db):
    result = airlines_over_two_flights_per_day(db)
    logger.info("Airlines over 2 flights computed")
    return result