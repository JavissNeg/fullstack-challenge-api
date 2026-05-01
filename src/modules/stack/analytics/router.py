from fastapi import APIRouter
from src.modules.stack.analytics.repository import fetch_stack_data
from src.modules.stack.analytics.service import (
    get_analytics_stats,
    get_analytics_highest_reputation,
    get_analytics_lowest_views,
    get_analytics_oldest,
    get_analytics_newest
)

router = APIRouter(tags=["stack-analytics"])

async def _get_items(query: str = "perl", order: str = "desc", sort: str = "activity"):
    return await fetch_stack_data(query=query, order=order, sort=sort)

@router.get("/stats")
async def analytics_stats(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_stats(items)

@router.get("/highest-reputation")
async def analytics_highest_reputation(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_highest_reputation(items)

@router.get("/lowest-views")
async def analytics_lowest_views(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_lowest_views(items)

@router.get("/oldest")
async def analytics_oldest(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_oldest(items)

@router.get("/newest")
async def analytics_newest(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await _get_items(query=query, order=order, sort=sort)
    return get_analytics_newest(items)
