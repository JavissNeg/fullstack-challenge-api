import pytest

from src.modules.stack.analytics.service import (
    get_analytics_stats,
    get_analytics_highest_reputation,
    get_analytics_lowest_views,
    get_analytics_oldest,
    get_analytics_newest,
)
from src.modules.stack.analytics.exceptions import NoItemsFoundError


def test_get_analytics_stats_success(monkeypatch):
    items = [
        {"is_answered": True},
        {"is_answered": False},
        {"is_answered": True},
    ]

    logs = []
    monkeypatch.setattr(
        "src.modules.stack.analytics.service.logger.info",
        lambda msg: logs.append(msg)
    )

    result = get_analytics_stats(items)

    assert result == {
        "total": 3,
        "answered": 2,
        "not_answered": 1
    }
    assert "Stats computed" in logs


def test_get_analytics_highest_reputation_success():
    items = [
        {"owner": {"reputation": 10}},
        {"owner": {"reputation": 100}},
        {"owner": {"reputation": 50}},
    ]

    result = get_analytics_highest_reputation(items)

    assert result["owner"]["reputation"] == 100


def test_get_analytics_lowest_views_success():
    items = [
        {"view_count": 200},
        {"view_count": 10},
        {"view_count": 50},
    ]

    result = get_analytics_lowest_views(items)

    assert result["view_count"] == 10


def test_get_analytics_oldest_success():
    items = [
        {"creation_date": 100},
        {"creation_date": 10},
        {"creation_date": 50},
    ]

    result = get_analytics_oldest(items)

    assert result["creation_date"] == 10


def test_get_analytics_newest_success():
    items = [
        {"creation_date": 100},
        {"creation_date": 10},
        {"creation_date": 500},
    ]

    result = get_analytics_newest(items)

    assert result["creation_date"] == 500


def test_get_analytics_raises_on_empty():
    with pytest.raises(NoItemsFoundError):
        get_analytics_stats([])