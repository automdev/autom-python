"""Official Python SDK for the Autom API."""

from ._endpoints import ENDPOINTS
from ._version import __version__
from .client import (
    DEFAULT_BASE_URL,
    DEFAULT_CONCURRENCY,
    DEFAULT_RETRY_DELAY,
    DEFAULT_TIMEOUT,
    MAX_RETRIES,
    RETRY_BACKOFF_FACTOR,
    AsyncAutomClient,
    AutomClient,
)
from .errors import (
    AutomAPIError,
    AutomConfigurationError,
    AutomError,
    AutomJobTimeoutError,
    AutomResponseDecodingError,
    AutomSerializationError,
    AutomTransportError,
)
from .models import (
    APIResponse,
    BatchResult,
    BinaryResponse,
    EndpointDefinition,
    HTTPMethod,
    JsonResponse,
    RawResponse,
    RequestOptions,
)

__all__ = [
    "APIResponse",
    "AsyncAutomClient",
    "BatchResult",
    "BinaryResponse",
    "DEFAULT_BASE_URL",
    "DEFAULT_CONCURRENCY",
    "DEFAULT_RETRY_DELAY",
    "DEFAULT_TIMEOUT",
    "MAX_RETRIES",
    "RETRY_BACKOFF_FACTOR",
    "ENDPOINTS",
    "EndpointDefinition",
    "HTTPMethod",
    "JsonResponse",
    "RawResponse",
    "RequestOptions",
    "AutomAPIError",
    "AutomClient",
    "AutomConfigurationError",
    "AutomError",
    "AutomJobTimeoutError",
    "AutomResponseDecodingError",
    "AutomSerializationError",
    "AutomTransportError",
    "__version__",
]
