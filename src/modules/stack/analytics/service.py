from src.modules.stack.analytics.repository import fetch_stack_data
from src.core.logging import get_logger

logger = get_logger(__name__)


def get_stats(items):
    answered = sum(1 for i in items if i.get("is_answered"))
    return {
        "total": len(items),
        "answered": answered,
        "not_answered": len(items) - answered
    }


def get_highest_reputation(items):
    item = max(items, key=lambda x: x.get("owner", {}).get("reputation", 0))
    owner = item.get("owner", {})
    return {
        "user": owner.get("display_name"),
        "reputation": owner.get("reputation"),
        "question": item.get("title")
    }


def get_lowest_views(items):
    item = min(items, key=lambda x: x.get("view_count", 0))
    return {
        "title": item.get("title"),
        "views": item.get("view_count")
    }


def get_oldest(items):
    item = min(items, key=lambda x: x.get("creation_date", float("inf")))
    return {
        "title": item.get("title"),
        "creation_date": item.get("creation_date")
    }


def get_newest(items):
    item = max(items, key=lambda x: x.get("creation_date", 0))
    return {
        "title": item.get("title"),
        "creation_date": item.get("creation_date")
    }


async def get_full_analytics(query: str = "perl", order: str = "desc", sort: str = "activity"):
    items = await fetch_stack_data(query=query, order=order, sort=sort)

    return {
        "stats": get_stats(items),
        "highest_reputation": get_highest_reputation(items),
        "lowest_views": get_lowest_views(items),
        "oldest": get_oldest(items),
        "newest": get_newest(items),
    }


def get_analytics_stats(items):
    logger.info(f"Stack stats - total items: {len(items)}")
    return get_stats(items)


def get_analytics_highest_reputation(items):
    result = get_highest_reputation(items)
    logger.info(f"Highest reputation: {result['user']} - {result['reputation']}")
    return result


def get_analytics_lowest_views(items):
    result = get_lowest_views(items)
    logger.info(f"Lowest views: {result['title']} - {result['views']} views")
    return result


def get_analytics_oldest(items):
    result = get_oldest(items)
    logger.info(f"Oldest: {result['title']} - {result['creation_date']}")
    return result


def get_analytics_newest(items):
    result = get_newest(items)
    logger.info(f"Newest: {result['title']} - {result['creation_date']}")
    return result