from src.modules.stack.analytics.repository import StackClient
from src.modules.stack.analytics.exceptions import NoItemsFoundError
from src.core.logging import get_logger

logger = get_logger(__name__)


def require_items(items):
    if not items:
        raise NoItemsFoundError("No items found")
    return items


def _run(items, fn, log_msg: str):
    items = require_items(items)
    result = fn(items)
    logger.info(log_msg)
    return result


def get_stats(items):
    total = len(items)
    answered = sum(1 for i in items if i.get("is_answered"))

    return {
        "total": total,
        "answered": answered,
        "not_answered": total - answered
    }


def get_highest_reputation(items):
    return max(items, key=lambda x: x.get("owner", {}).get("reputation", 0))


def get_lowest_views(items):
    return min(items, key=lambda x: x.get("view_count", 0))


def get_oldest(items):
    return min(items, key=lambda x: x.get("creation_date", float("inf")))


def get_newest(items):
    return max(items, key=lambda x: x.get("creation_date", 0))


def get_analytics_stats(items):
    return _run(items, get_stats, "Stats computed")


def get_analytics_highest_reputation(items):
    return _run(items, get_highest_reputation, "Highest reputation computed")


def get_analytics_lowest_views(items):
    return _run(items, get_lowest_views, "Lowest views computed")


def get_analytics_oldest(items):
    return _run(items, get_oldest, "Oldest item computed")


def get_analytics_newest(items):
    return _run(items, get_newest, "Newest item computed")


async def get_items(query: str, order: str, sort: str):
    async with StackClient() as client:
        return await client.fetch_stack_data(
            query=query,
            order=order,
            sort=sort
        )