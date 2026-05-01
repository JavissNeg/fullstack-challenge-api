import httpx
from src.core.logging import get_logger

logger = get_logger(__name__)

STACK_API_URL = "https://api.stackexchange.com/2.2/search/advanced"


async def fetch_stack_data(
    query: str = "perl",
    pagesize: int = 50,
    order: str = "desc",
    sort: str = "activity"
):
    params = {
        "order": order,
        "sort": sort,
        "intitle": query,
        "site": "stackoverflow",
        "pagesize": pagesize,
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(STACK_API_URL, params=params)
            response.raise_for_status()
            return response.json().get("items", [])
    except httpx.HTTPError as e:
        logger.error(f"HTTP error fetching Stack data: {e}")
        return []