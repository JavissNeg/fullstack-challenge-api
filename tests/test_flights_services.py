import pytest
from types import SimpleNamespace

from src.modules.flights.analytics.repository import (
    top_airport,
    airlines_over_two_flights_per_day,
)
from src.modules.flights.analytics.service import (
    get_top_airport,
)
from src.modules.flights.analytics.exceptions import NoFlightDataFoundError


class FakeSubquery:
    def __init__(self):
        self.c = SimpleNamespace(
            airline="airline",
            day="day"
        )


class FakeQuery:
    def __init__(self, result=None, results=None):
        self._result = result
        self._results = results or []

    def join(self, *args, **kwargs): return self
    def group_by(self, *args, **kwargs): return self
    def order_by(self, *args, **kwargs): return self
    def having(self, *args, **kwargs): return self

    def subquery(self):
        return FakeSubquery()

    def first(self): return self._result
    def all(self): return self._results

class FakeDB:
    def __init__(self, query_obj):
        self.query_obj = query_obj

    def query(self, *args, **kwargs):
        return self.query_obj


def test_top_airport_success():
    fake_row = SimpleNamespace(airport="MEX", total_movement=120)
    db = FakeDB(FakeQuery(result=fake_row))

    result = top_airport(db)

    assert result == {
        "airport": "MEX",
        "total_movement": 120
    }


def test_top_airport_no_data():
    db = FakeDB(FakeQuery(result=None))

    with pytest.raises(NoFlightDataFoundError):
        top_airport(db)


def test_airlines_over_two_success():
    fake_rows = [
        SimpleNamespace(airline="Volaris", days_with_over_two_flights=3)
    ]
    db = FakeDB(FakeQuery(results=fake_rows))

    result = airlines_over_two_flights_per_day(db)

    assert result == [
        {
            "airline": "Volaris",
            "days_with_over_two_flights": 3
        }
    ]


def test_airlines_over_two_no_data():
    db = FakeDB(FakeQuery(results=[]))

    with pytest.raises(NoFlightDataFoundError):
        airlines_over_two_flights_per_day(db)


def test_get_top_airport_calls_repo_and_logs(monkeypatch):
    expected = {"airport": "MEX", "total_movement": 100}

    monkeypatch.setattr(
        "src.modules.flights.analytics.service.top_airport",
        lambda db: expected
    )

    logs = []
    monkeypatch.setattr(
        "src.modules.flights.analytics.service.logger.info",
        lambda msg: logs.append(msg)
    )

    result = get_top_airport(None)

    assert result == expected
    assert "Top airport computed" in logs