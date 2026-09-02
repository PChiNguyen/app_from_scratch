# core/exceptions.py
from typing import Any, Optional
from fastapi import status


class AppException(Exception):
    """
    Base exception class for all application domain errors.
    Carries an HTTP status code and detail message for central handling.
    """             
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        payload: Optional[Any] = None
    ):
        self.message = message
        self.status_code = status_code
        self.payload = payload
        super().__init__(self.message)


class DatabaseValidationError(AppException):
    """Raised when data fails database constraint or validation rules (400 Bad Request)."""
    def __init__(self, message: str, payload: Optional[Any] = None):
        super().__init__(
            message=message,
            status_code=status.HTTP_400_BAD_REQUEST,
            payload=payload
        )


class ResourceNotFoundError(AppException):
    """Raised when a database record (Student, Template, Score) is missing (404 Not Found)."""
    def __init__(self, message: str = "The requested resource was not found."):
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND
        )


class ConflictError(AppException):
    """Raised when a unique resource constraint is violated, like a duplicate ID (409 Conflict)."""
    def __init__(self, message: str = "Resource already exists."):
        super().__init__(
            message=message,
            status_code=status.HTTP_409_CONFLICT
        )


class AuthenticationError(AppException):
    """Raised when JWT verification fails or credentials are invalid (401 Unauthorized)."""
    def __init__(self, message: str = "Could not validate credentials."):
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class ForbiddenError(AppException):
    """Raised when an authenticated user lacks RBAC permissions (403 Forbidden)."""
    def __init__(self, message: str = "You do not have permission to perform this action."):
        super().__init__(
            message=message,
            status_code=status.HTTP_403_FORBIDDEN
        )


class UnprocessableEntityError(AppException):
    """Raised when business logic validation fails even if input format is valid (422 Unprocessable Entity)."""
    def __init__(self, message: str = "Unprocessable entity business logic failure.", payload: Optional[Any] = None):
        super().__init__(
            message=message,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            payload=payload
        )


class RateLimitExceededError(AppException):
    """Raised when a user or IP exceeds API rate limits (429 Too Many Requests)."""
    def __init__(self, message: str = "Rate limit exceeded. Please try again later."):
        super().__init__(
            message=message,
            status_code=status.HTTP_429_TOO_MANY_REQUESTS
        )


class ThirdPartyServiceError(AppException):
    """Raised when external integrations (Email, Payment, OpenAI/Gemini) fail (502 Bad Gateway)."""
    def __init__(self, message: str = "External service request failed."):
        super().__init__(
            message=message,
            status_code=status.HTTP_502_BAD_GATEWAY
        )


class ServiceUnavailableError(AppException):
    """Raised when critical infrastructure (Database, Redis, Worker) is unreachable (503 Service Unavailable)."""
    def __init__(self, message: str = "Service temporarily unavailable. Please try again later."):
        super().__init__(
            message=message,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )


class InternalServerError(AppException):
    """Raised when an unhandled server error occurs safely hiding sensitive stack traces (500 Internal Server Error)."""
    def __init__(self, message: str = "An unexpected internal error occurred."):
        super().__init__(
            message=message,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )