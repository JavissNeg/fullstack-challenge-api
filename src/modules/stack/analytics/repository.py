import httpx
from typing import Any, List, Dict, Optional
from src.core.logging import get_logger

logger = get_logger(__name__)

STACK_API_URL = "https://api.stackexchange.com/2.3/search/advanced"


class StackClient:
    def __init__(
        self,
        base_url: str = STACK_API_URL,
        timeout: float = 10.0,
        max_retries: int = 3,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._client:
            await self._client.aclose()

    async def fetch_stack_data(
        self,
        query: str = "perl",
        pagesize: int = 50,
        order: str = "desc",
        sort: str = "activity",
    ) -> List[Dict[str, Any]]:
        if not self._client:
            raise RuntimeError("Client not initialized. Use 'async with'.")

        params = {
            "order": order,
            "sort": sort,
            "intitle": query,
            "site": "stackoverflow",
            "pagesize": pagesize,
        }

        for attempt in range(1, self.max_retries + 1):
            try:
                response = await self._client.get(self.base_url, params=params)
                response.raise_for_status()

                data = response.json()
                return data.get("items", [])

            except httpx.TimeoutException:
                logger.warning(
                    "Timeout fetching Stack data (attempt %d/%d) | query=%s",
                    attempt,
                    self.max_retries,
                    query,
                )

            except httpx.HTTPStatusError as e:
                logger.error(
                    "HTTP error %s fetching Stack data | query=%s | response=%s",
                    e.response.status_code,
                    query,
                    e.response.text,
                )
                break  

            except httpx.RequestError as e:
                logger.warning(
                    "Request error fetching Stack data (attempt %d/%d): %s",
                    attempt,
                    self.max_retries,
                    str(e),
                )

        return []