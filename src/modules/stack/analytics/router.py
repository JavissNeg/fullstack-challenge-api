from fastapi import APIRouter, Query

from .schemas import StackStats, HighestReputation, LowestViews, QuestionAge

from src.modules.stack.analytics.service import (
    get_items,
    get_analytics_stats,
    get_analytics_highest_reputation,
    get_analytics_lowest_views,
    get_analytics_oldest,
    get_analytics_newest,
)
    
router = APIRouter(
    tags=["Stack Analytics"]
)

def common_query():
    return Query("perl", description="Término de búsqueda en títulos")


def common_order():
    return Query("desc", description="Orden: asc o desc")


def common_sort():
    return Query("activity", description="Sort: activity, votes, creation")


async def _fetch(query: str, order: str, sort: str):
    return await get_items(query, order, sort)


@router.get(
    "/stats",
    response_model=StackStats,
    summary="Estadísticas generales",
    responses={404: {"description": "No se encontraron resultados"}},
)
async def analytics_stats(
    query: str = common_query(),
    order: str = common_order(),
    sort: str = common_sort(),
):
    items = await _fetch(query, order, sort)
    return get_analytics_stats(items)


@router.get(
    "/highest-reputation",
    response_model=HighestReputation,
    summary="Usuario con mayor reputación",
    responses={404: {"description": "No se encontraron resultados"}},
)
async def analytics_highest_reputation(
    query: str = common_query(),
    order: str = common_order(),
    sort: str = common_sort(),
):
    items = await _fetch(query, order, sort)
    return get_analytics_highest_reputation(items)


@router.get(
    "/lowest-views",
    response_model=LowestViews,
    summary="Pregunta con menos vistas",
    responses={404: {"description": "No se encontraron resultados"}},
)
async def analytics_lowest_views(
    query: str = common_query(),
    order: str = common_order(),
    sort: str = common_sort(),
):
    items = await _fetch(query, order, sort)
    return get_analytics_lowest_views(items)


@router.get(
    "/oldest",
    response_model=QuestionAge,
    summary="Pregunta más antigua",
    responses={404: {"description": "No se encontraron resultados"}},
)
async def analytics_oldest(
    query: str = common_query(),
    order: str = common_order(),
    sort: str = common_sort(),
):
    items = await _fetch(query, order, sort)
    return get_analytics_oldest(items)


@router.get(
    "/newest",
    response_model=QuestionAge,
    summary="Pregunta más reciente",
    responses={404: {"description": "No se encontraron resultados"}},
)
async def analytics_newest(
    query: str = common_query(),
    order: str = common_order(),
    sort: str = common_sort(),
):
    items = await _fetch(query, order, sort)
    return get_analytics_newest(items)