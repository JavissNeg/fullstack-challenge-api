from fastapi import APIRouter, Query
from .schemas import StackStats, HighestReputation, LowestViews, QuestionAge
from src.modules.stack.analytics.repository import fetch_stack_data
from src.modules.stack.analytics.service import (
    get_analytics_stats,
    get_analytics_highest_reputation,
    get_analytics_lowest_views,
    get_analytics_oldest,
    get_analytics_newest
)

router = APIRouter()

async def _get_items(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    return await fetch_stack_data(query=query, order=order, sort=sort)

@router.get(
    "/stats",
    response_model=StackStats,
    summary="Estadísticas de preguntas de Stack Exchange",
    description="Obtiene estadísticas resumidas de preguntas encontradas en la búsqueda.",
    response_description="Estadísticas de preguntas"
)
async def analytics_stats(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_stats(items)

@router.get(
    "/highest-reputation",
    response_model=HighestReputation,
    summary="Usuario con mayor reputación",
    description="Encuentra el usuario con mayor reputación entre los propietarios de preguntas.",
    response_description="Usuario con mayor reputación"
)
async def analytics_highest_reputation(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_highest_reputation(items)

@router.get(
    "/lowest-views",
    response_model=LowestViews,
    summary="Pregunta con menos vistas",
    description="Encuentra la pregunta con menor número de vistas.",
    response_description="Pregunta menos vista"
)
async def analytics_lowest_views(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_lowest_views(items)

@router.get(
    "/oldest",
    response_model=QuestionAge,
    summary="Pregunta más antigua",
    description="Encuentra la pregunta más antigua por fecha de creación.",
    response_description="Pregunta más antigua"
)
async def analytics_oldest(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_oldest(items)

@router.get(
    "/newest",
    response_model=QuestionAge,
    summary="Pregunta más reciente",
    description="Encuentra la pregunta más recientemente creada.",
    response_description="Pregunta más reciente"
)
async def analytics_newest(
    query: str = Query("perl", description="Término de búsqueda en títulos de preguntas"),
    order: str = Query("desc", description="Orden de clasificación: asc o desc"),
    sort: str = Query("activity", description="Criterio de ordenación: activity, votes, creation")
):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_newest(items)
