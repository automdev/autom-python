"""Generated from the Autom OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from .models import EndpointDefinition

ENDPOINTS: dict[str, EndpointDefinition] = {
    "bing_search": EndpointDefinition(
        path="/v1/bing/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "brave_images": EndpointDefinition(
        path="/v1/brave/images",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "brave_search": EndpointDefinition(
        path="/v1/brave/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "brave_videos": EndpointDefinition(
        path="/v1/brave/videos",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "duckduckgo_search": EndpointDefinition(
        path="/v1/duckduckgo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "finder_google_countries": EndpointDefinition(
        path="/v1/finder/google-countries",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "finder_google_languages": EndpointDefinition(
        path="/v1/finder/google-languages",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "finder_google_locations": EndpointDefinition(
        path="/v1/finder/google-locations",
        methods=("GET",),
        response="json",
        required=("query",),
    ),
    "google_images": EndpointDefinition(
        path="/v1/google/images",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_jobs": EndpointDefinition(
        path="/v1/google/jobs",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_maps": EndpointDefinition(
        path="/v1/google/maps",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_news": EndpointDefinition(
        path="/v1/google/news",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search": EndpointDefinition(
        path="/v1/google/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search_ai": EndpointDefinition(
        path="/v1/google/search/ai",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search_autocomplete": EndpointDefinition(
        path="/v1/google/search/autocomplete",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_search_light": EndpointDefinition(
        path="/v1/google/search/light",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_shopping": EndpointDefinition(
        path="/v1/google/shopping",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "google_videos": EndpointDefinition(
        path="/v1/google/videos",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=(
            "query",
            "page",
        ),
    ),
    "jobs": EndpointDefinition(
        path="/v1/jobs/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "search": EndpointDefinition(
        path="/v1/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
    "stats": EndpointDefinition(
        path="/v1/stats",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "usage": EndpointDefinition(
        path="/v1/usage",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "yahoo_search": EndpointDefinition(
        path="/v1/yahoo/search",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("query",),
    ),
}
