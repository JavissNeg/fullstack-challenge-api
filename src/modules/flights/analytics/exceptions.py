from src.core.exceptions import AppException


class NoFlightDataFoundError(AppException):
    status_code = 404

    def __init__(self, message: str = "No flight data found"):
        super().__init__(message)


class DatabaseQueryError(AppException):
    status_code = 500

    def __init__(self, message: str = "Database query failed"):
        super().__init__(message)