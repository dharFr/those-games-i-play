from typing import Any, Dict, Optional

class AppException(Exception):
    """Base exception class for application errors."""
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(message)

class NotFoundException(AppException):
    """Raised when a resource is not found."""
    def __init__(self, resource: str, resource_id: Any):
        super().__init__(
            message=f"{resource} not found",
            status_code=404,
            details={"resource": resource, "id": resource_id}
        )

class ValidationError(AppException):
    """Raised when validation fails."""
    def __init__(self, message: str, details: Dict[str, Any]):
        super().__init__(
            message=message,
            status_code=400,
            details=details
        )

class ExternalAPIError(AppException):
    """Raised when an external API call fails."""
    def __init__(self, service: str, message: str):
        super().__init__(
            message=f"{service} API error: {message}",
            status_code=502,
            details={"service": service}
        )
