"""Call any path with request() and handle API errors."""

from autom import AutomAPIError, AutomClient, JsonResponse

with AutomClient() as client:  # reads AUTOM_API_KEY
    try:
        response = client.request("GET", "/v1/usage")
        if isinstance(response, JsonResponse):
            print(response.data)
    except AutomAPIError as error:
        print(f"HTTP {error.status}: {error}")
