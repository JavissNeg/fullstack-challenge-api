from src.core.exceptions import AppException


class NoItemsFoundError(AppException):
    status_code = 404

    def __init__(self, message: str = "No items found"):
        super().__init__(message)