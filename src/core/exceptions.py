class AppException(Exception):
    status_code = 500

    def __init__(self, message: str = "Application error"):
        super().__init__(message)
        self.message = message