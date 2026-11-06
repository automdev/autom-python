"""Generated from the Autom OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from typing import Any, cast

from .models import APIResponse, JsonResponse, RequestOptions


class _SyncOperations:
    """Generated Autom endpoint methods."""

    __slots__ = ()

    def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    def bing_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        num: int | float | None = None,
        location: str | None = None,
        lat: int | float | None = None,
        lon: int | float | None = None,
        mkt: str | None = None,
        cc: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Bing Search. Query Bing Search via API and retrieve structured organic results (title, link, snippet, position). Credit cost: 1 credit per call.

        ``GET / POST /v1/bing/search``

        Args:
            query: The search query you want to run on Bing.
            page: Page number for pagination (1 = first page).
            num: Number of results per page (e.g. 10, 20, 50). This value is a suggestion.
            location: Search origin location (e.g. city).
            lat: GPS latitude for the search origin.
            lon: GPS longitude for the search origin.
            mkt: Market code where results come from (e.g. en-US). Cannot be used together with cc.
            cc: Country code to search from (2-letter ISO 3166-1). Cannot be used together with mkt.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "bing_search",
                {
                    "query": query,
                    "page": page,
                    "num": num,
                    "location": location,
                    "lat": lat,
                    "lon": lon,
                    "mkt": mkt,
                    "cc": cc,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def brave_images(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Images. Search Brave Images via API and retrieve structured image results with pagination and SafeSearch. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/images``

        Args:
            query: The search query you want to run on Brave Images.
            page: Page number for pagination (50 results per page).
            gl: Country code (e.g. fr, us). Mapped to Brave country.
            hl: Language code (e.g. fr, en). Mapped to Brave lang.
            safe: SafeSearch: active | off | moderate | strict. Google-style active maps to Brave strict.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "brave_images",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def brave_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Search. Search Brave Search via API and retrieve structured organic results with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/search``

        Args:
            query: The search query you want to run on Brave Search.
            page: Page number for pagination.
            gl: Country code, for example us, fr, gb, de.
            hl: Language code, for example en, fr, de.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "brave_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def brave_videos(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Videos. Search Brave Videos via API and retrieve structured video results with pagination and SafeSearch. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/videos``

        Args:
            query: The search query you want to run on Brave Videos.
            page: Page number for pagination.
            gl: Country code (e.g. fr, us). Mapped to Brave country.
            hl: Language code (e.g. fr, en). Mapped to Brave lang.
            safe: SafeSearch: active | off | moderate | strict. Google-style active maps to Brave strict.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "brave_videos",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def duckduckgo_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """DuckDuckGo Search. Query DuckDuckGo via API and retrieve structured organic results with region and language. Credit cost: 1 credit per call.

        ``GET / POST /v1/duckduckgo/search``

        Args:
            query: Search query sent to DuckDuckGo Search.
            page: Page number. Page 1 is the first page of results.
            gl: Country code, for example us, fr, gb, de, jp.
            hl: Language code, for example en, fr, de, ja, zh.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "duckduckgo_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def finder_google_countries(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Countries. Search Google countries and retrieve country codes (free Finder endpoint).

        ``GET /v1/finder/google-countries``

        Args:
            query: Filter countries by a search string (case-insensitive). Returns all countries whose code or name matches the specified query.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "finder_google_countries",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    def finder_google_languages(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Languages. Search Google languages and retrieve language codes (free Finder endpoint).

        ``GET /v1/finder/google-languages``

        Args:
            query: Filter languages by a search string (case-insensitive). Returns all languages whose names contain the specified string.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "finder_google_languages",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    def finder_google_locations(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Locations. Find supported Google locations and retrieve location IDs and country codes (free endpoint).

        ``GET /v1/finder/google-locations``

        Args:
            query: Search locations supported by Piloterr (cities, countries, etc.) by providing a query string. Returns matching locations ordered by reach.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "finder_google_locations",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    def google_images(
        self,
        *,
        query: str,
        page: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        async_: bool | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Images. Search Google Images via API and retrieve image results (URLs, titles, sources, dimensions). Credit cost: 1 credit per call.

        ``GET / POST /v1/google/images``

        Args:
            query: Query you want to search on Google Images (e.g. "lion", "nike logo", "modern house exterior").
            page: Page number for pagination (1 = first page).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            async_: If true, returns a job and lets you fetch results asynchronously.
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_images",
                {
                    "query": query,
                    "page": page,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "async": async_,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_jobs(
        self,
        *,
        query: str,
        uds: str | None = None,
        lrad: int | float | None = None,
        ltype: int | float | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        next_page_token: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Jobs. Scrape Google Jobs results via API and retrieve structured job listings with title, company, location, and pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/jobs``

        Args:
            query: The job search query to run on Google Jobs (e.g. developer, barista new york).
            uds: Advanced search filters string for Google Jobs (encoded filter chips).
            lrad: Search radius in kilometers. Does not strictly limit the radius, but influences result proximity.
            ltype: Filter results by work type. Set to 1 to filter for work from home / remote jobs.
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            next_page_token: Token to fetch the next page of results. Returned in the serpapi_pagination.next_page_token field of the previous response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_jobs",
                {
                    "query": query,
                    "uds": uds,
                    "lrad": lrad,
                    "ltype": ltype,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "next_page_token": next_page_token,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_maps(
        self,
        *,
        query: str,
        page: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        ll: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Maps. Search Google Maps via API and retrieve structured place results (address, website, phone). Credit cost: 1 credit per call.

        ``GET / POST /v1/google/maps``

        Args:
            query: Search query for Google Maps (e.g. business type, brand, or place name).
            page: Page number for pagination (1 = first page).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            ll: Map center / geo hint in Google format (e.g. @43.5131985,1.4600501,60m). Helps focus results around a coordinate and zoom radius.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_maps",
                {
                    "query": query,
                    "page": page,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "ll": ll,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_news(
        self,
        *,
        query: str,
        page: int | float | None = None,
        num: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google News. Search Google News via API and retrieve structured news results with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/news``

        Args:
            query: Query to search on Google News (keywords, company, topic).
            page: Page number for pagination (1 = first page).
            num: Maximum number of results per page (e.g. 10).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_news",
                {
                    "query": query,
                    "page": page,
                    "num": num,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_search(
        self,
        *,
        query: str,
        tbs: str | None = None,
        safe: str | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        page: int | float | None = None,
        num: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search. Scrape Google Search results via API and retrieve structured SERP data with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search``

        Args:
            query: The search query you want to run on Google (supports advanced operators like site:, inurl:, intitle:).
            tbs: Advanced search filters string (e.g. time ranges: qdr:h last hour, qdr:d last day, qdr:w last week, qdr:m last month, qdr:y last year).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            page: Page number / offset used for pagination.
            num: Maximum number of results to return per page (deprecated).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_search",
                {
                    "query": query,
                    "tbs": tbs,
                    "safe": safe,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "page": page,
                    "num": num,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_search_ai(
        self,
        *,
        query: str,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google AI Mode. Query Google AI Mode via API. JSON with text_blocks, references, and shopping_results. Credit cost: 3 credits per call.

        ``GET / POST /v1/google/search/ai``

        Args:
            query: The question or search query you want Google AI Mode to answer (supports advanced operators like site:, inurl:, intitle:).
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_search_ai",
                {
                    "query": query,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_search_autocomplete(
        self,
        *,
        query: str,
        cp: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search Autocomplete. Get Google Search autocomplete suggestions via API for a given query. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search/autocomplete``

        Args:
            query: The search query for which you want to get autocomplete suggestions.
            cp: Cursor position in the search query where you want to get autocomplete suggestions.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_search_autocomplete",
                {
                    "query": query,
                    "cp": cp,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_search_light(
        self,
        *,
        query: str,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search Light. Scrape lightweight Google Search results via API: fast, cost-efficient, organic results only. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search/light``

        Args:
            query: The search query you want to run on Google (supports advanced operators like site:, inurl:, intitle:).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_search_light",
                {
                    "query": query,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_shopping(
        self,
        *,
        query: str,
        page: int | float | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Shopping. Scrape Google Shopping results via API and retrieve structured product listings with prices, ratings, and merchant data. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/shopping``

        Args:
            query: Query to search on Google Shopping (product name, brand, category).
            page: Page number for pagination (1 = first page).
            location: Location to localize results (e.g. New York, United States). Generates a UULE parameter automatically.
            uule: Encoded location parameter (UULE). Use location instead if you don't have a pre-encoded value.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_shopping",
                {
                    "query": query,
                    "page": page,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def google_videos(
        self,
        *,
        query: str,
        page: int | float,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        num: int | float | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Videos. Search Google Videos via API and retrieve structured video results with metadata. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/videos``

        Args:
            query: The search query you want to run on Google Videos.
            location: Human-readable location to originate the search from. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            page: Page number for pagination (1 = first page).
            num: Maximum number of results per page (e.g. 10).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "google_videos",
                {
                    "query": query,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "page": page,
                    "num": num,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, self._call("jobs", {"id": id}, request_options))

    def search(
        self,
        *,
        query: str,
        engines: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Search. One call walks engines in order and returns the first organic results. engines=auto tries Google, then Brave, Bing, DuckDuckGo, Yahoo, and Baidu. Omitted gl is us and omitted hl is en. There is no page parameter: the response is always pag… Credit cost: 1 credit per call.

        ``GET / POST /v1/search``

        Args:
            query: Search query.
            engines: Engine order. Default auto tries google, brave, bing, duckduckgo, yahoo, then baidu. A comma-separated list is followed as given. ddg and duck mean duckduckgo. Unknown names are ignored.
            gl: Country code. Defaults to us when omitted. For example us, fr, gb, de.
            hl: Language code. Defaults to en when omitted. For example en, fr, de.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "search",
                {
                    "query": query,
                    "engines": engines,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example google. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/google/search. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse, self._call("stats", {"engine": engine, "path": path}, request_options)
        )

    def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your Autom account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, self._call("usage", {}, request_options))

    def yahoo_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Yahoo Search. Query Yahoo via API and retrieve structured organic results with country and language. Credit cost: 1 credit per call.

        ``GET / POST /v1/yahoo/search``

        Args:
            query: Search query sent to Yahoo Search.
            page: Page number. Page 1 is the first page of results.
            gl: Country code, for example us, fr, gb, de, jp.
            hl: Language code, for example en, fr, de, ja, zh.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "yahoo_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )


class _AsyncOperations:
    """Generated Autom endpoint methods."""

    __slots__ = ()

    async def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    async def bing_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        num: int | float | None = None,
        location: str | None = None,
        lat: int | float | None = None,
        lon: int | float | None = None,
        mkt: str | None = None,
        cc: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Bing Search. Query Bing Search via API and retrieve structured organic results (title, link, snippet, position). Credit cost: 1 credit per call.

        ``GET / POST /v1/bing/search``

        Args:
            query: The search query you want to run on Bing.
            page: Page number for pagination (1 = first page).
            num: Number of results per page (e.g. 10, 20, 50). This value is a suggestion.
            location: Search origin location (e.g. city).
            lat: GPS latitude for the search origin.
            lon: GPS longitude for the search origin.
            mkt: Market code where results come from (e.g. en-US). Cannot be used together with cc.
            cc: Country code to search from (2-letter ISO 3166-1). Cannot be used together with mkt.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "bing_search",
                {
                    "query": query,
                    "page": page,
                    "num": num,
                    "location": location,
                    "lat": lat,
                    "lon": lon,
                    "mkt": mkt,
                    "cc": cc,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def brave_images(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Images. Search Brave Images via API and retrieve structured image results with pagination and SafeSearch. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/images``

        Args:
            query: The search query you want to run on Brave Images.
            page: Page number for pagination (50 results per page).
            gl: Country code (e.g. fr, us). Mapped to Brave country.
            hl: Language code (e.g. fr, en). Mapped to Brave lang.
            safe: SafeSearch: active | off | moderate | strict. Google-style active maps to Brave strict.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "brave_images",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def brave_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Search. Search Brave Search via API and retrieve structured organic results with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/search``

        Args:
            query: The search query you want to run on Brave Search.
            page: Page number for pagination.
            gl: Country code, for example us, fr, gb, de.
            hl: Language code, for example en, fr, de.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "brave_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def brave_videos(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Brave Videos. Search Brave Videos via API and retrieve structured video results with pagination and SafeSearch. Credit cost: 1 credit per call.

        ``GET / POST /v1/brave/videos``

        Args:
            query: The search query you want to run on Brave Videos.
            page: Page number for pagination.
            gl: Country code (e.g. fr, us). Mapped to Brave country.
            hl: Language code (e.g. fr, en). Mapped to Brave lang.
            safe: SafeSearch: active | off | moderate | strict. Google-style active maps to Brave strict.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "brave_videos",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def duckduckgo_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """DuckDuckGo Search. Query DuckDuckGo via API and retrieve structured organic results with region and language. Credit cost: 1 credit per call.

        ``GET / POST /v1/duckduckgo/search``

        Args:
            query: Search query sent to DuckDuckGo Search.
            page: Page number. Page 1 is the first page of results.
            gl: Country code, for example us, fr, gb, de, jp.
            hl: Language code, for example en, fr, de, ja, zh.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "duckduckgo_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def finder_google_countries(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Countries. Search Google countries and retrieve country codes (free Finder endpoint).

        ``GET /v1/finder/google-countries``

        Args:
            query: Filter countries by a search string (case-insensitive). Returns all countries whose code or name matches the specified query.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "finder_google_countries",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    async def finder_google_languages(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Languages. Search Google languages and retrieve language codes (free Finder endpoint).

        ``GET /v1/finder/google-languages``

        Args:
            query: Filter languages by a search string (case-insensitive). Returns all languages whose names contain the specified string.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "finder_google_languages",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    async def finder_google_locations(
        self,
        *,
        query: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Locations. Find supported Google locations and retrieve location IDs and country codes (free endpoint).

        ``GET /v1/finder/google-locations``

        Args:
            query: Search locations supported by Piloterr (cities, countries, etc.) by providing a query string. Returns matching locations ordered by reach.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "finder_google_locations",
                {"query": query, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    async def google_images(
        self,
        *,
        query: str,
        page: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        async_: bool | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Images. Search Google Images via API and retrieve image results (URLs, titles, sources, dimensions). Credit cost: 1 credit per call.

        ``GET / POST /v1/google/images``

        Args:
            query: Query you want to search on Google Images (e.g. "lion", "nike logo", "modern house exterior").
            page: Page number for pagination (1 = first page).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            async_: If true, returns a job and lets you fetch results asynchronously.
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_images",
                {
                    "query": query,
                    "page": page,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "async": async_,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_jobs(
        self,
        *,
        query: str,
        uds: str | None = None,
        lrad: int | float | None = None,
        ltype: int | float | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        next_page_token: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Jobs. Scrape Google Jobs results via API and retrieve structured job listings with title, company, location, and pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/jobs``

        Args:
            query: The job search query to run on Google Jobs (e.g. developer, barista new york).
            uds: Advanced search filters string for Google Jobs (encoded filter chips).
            lrad: Search radius in kilometers. Does not strictly limit the radius, but influences result proximity.
            ltype: Filter results by work type. Set to 1 to filter for work from home / remote jobs.
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            next_page_token: Token to fetch the next page of results. Returned in the serpapi_pagination.next_page_token field of the previous response.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_jobs",
                {
                    "query": query,
                    "uds": uds,
                    "lrad": lrad,
                    "ltype": ltype,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "next_page_token": next_page_token,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_maps(
        self,
        *,
        query: str,
        page: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        ll: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Maps. Search Google Maps via API and retrieve structured place results (address, website, phone). Credit cost: 1 credit per call.

        ``GET / POST /v1/google/maps``

        Args:
            query: Search query for Google Maps (e.g. business type, brand, or place name).
            page: Page number for pagination (1 = first page).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            ll: Map center / geo hint in Google format (e.g. @43.5131985,1.4600501,60m). Helps focus results around a coordinate and zoom radius.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_maps",
                {
                    "query": query,
                    "page": page,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "ll": ll,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_news(
        self,
        *,
        query: str,
        page: int | float | None = None,
        num: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google News. Search Google News via API and retrieve structured news results with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/news``

        Args:
            query: Query to search on Google News (keywords, company, topic).
            page: Page number for pagination (1 = first page).
            num: Maximum number of results per page (e.g. 10).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_news",
                {
                    "query": query,
                    "page": page,
                    "num": num,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_search(
        self,
        *,
        query: str,
        tbs: str | None = None,
        safe: str | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        page: int | float | None = None,
        num: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search. Scrape Google Search results via API and retrieve structured SERP data with pagination. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search``

        Args:
            query: The search query you want to run on Google (supports advanced operators like site:, inurl:, intitle:).
            tbs: Advanced search filters string (e.g. time ranges: qdr:h last hour, qdr:d last day, qdr:w last week, qdr:m last month, qdr:y last year).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            page: Page number / offset used for pagination.
            num: Maximum number of results to return per page (deprecated).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_search",
                {
                    "query": query,
                    "tbs": tbs,
                    "safe": safe,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "page": page,
                    "num": num,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_search_ai(
        self,
        *,
        query: str,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google AI Mode. Query Google AI Mode via API. JSON with text_blocks, references, and shopping_results. Credit cost: 3 credits per call.

        ``GET / POST /v1/google/search/ai``

        Args:
            query: The question or search query you want Google AI Mode to answer (supports advanced operators like site:, inurl:, intitle:).
            location: Human-readable location to originate the search from (e.g. New York, NY, Paris, France). If several locations match, the most popular one is used. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Use for precise geo targeting. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_search_ai",
                {
                    "query": query,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_search_autocomplete(
        self,
        *,
        query: str,
        cp: int | float | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search Autocomplete. Get Google Search autocomplete suggestions via API for a given query. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search/autocomplete``

        Args:
            query: The search query for which you want to get autocomplete suggestions.
            cp: Cursor position in the search query where you want to get autocomplete suggestions.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_search_autocomplete",
                {
                    "query": query,
                    "cp": cp,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_search_light(
        self,
        *,
        query: str,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Search Light. Scrape lightweight Google Search results via API: fast, cost-efficient, organic results only. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/search/light``

        Args:
            query: The search query you want to run on Google (supports advanced operators like site:, inurl:, intitle:).
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_search_light",
                {
                    "query": query,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_shopping(
        self,
        *,
        query: str,
        page: int | float | None = None,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Shopping. Scrape Google Shopping results via API and retrieve structured product listings with prices, ratings, and merchant data. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/shopping``

        Args:
            query: Query to search on Google Shopping (product name, brand, category).
            page: Page number for pagination (1 = first page).
            location: Location to localize results (e.g. New York, United States). Generates a UULE parameter automatically.
            uule: Encoded location parameter (UULE). Use location instead if you don't have a pre-encoded value.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_shopping",
                {
                    "query": query,
                    "page": page,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def google_videos(
        self,
        *,
        query: str,
        page: int | float,
        location: str | None = None,
        uule: str | None = None,
        google_domain: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        cr: str | None = None,
        lr: str | None = None,
        num: int | float | None = None,
        safe: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Google Videos. Search Google Videos via API and retrieve structured video results with metadata. Credit cost: 1 credit per call.

        ``GET / POST /v1/google/videos``

        Args:
            query: The search query you want to run on Google Videos.
            location: Human-readable location to originate the search from. Note: location and uule cannot be used together.
            uule: Google encoded location parameter. Note: uule and location cannot be used together.
            google_domain: Google domain to use for the search. Defaults to google.com.
            gl: Country to use for the Google search. Two-letter country code (e.g. us for the United States, uk for United Kingdom, or fr for France).
            hl: Language to use for the Google search. Two or three-letter language code (e.g. en, es, fr), optionally followed by a region code (e.g. en-gb, es-419).
            cr: Limit results to one or more countries. Use country{XX} with | as delimiter (e.g. countryFR|countryDE).
            lr: Limit results to one or more languages. Use lang_{xx} with | as delimiter (e.g. lang_fr|lang_de).
            page: Page number for pagination (1 = first page).
            num: Maximum number of results per page (e.g. 10).
            safe: Adult content filter. active enables Google SafeSearch; off disables it. Omit to use Google default.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "google_videos",
                {
                    "query": query,
                    "location": location,
                    "uule": uule,
                    "google_domain": google_domain,
                    "gl": gl,
                    "hl": hl,
                    "cr": cr,
                    "lr": lr,
                    "page": page,
                    "num": num,
                    "safe": safe,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, await self._call("jobs", {"id": id}, request_options))

    async def search(
        self,
        *,
        query: str,
        engines: str | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Search. One call walks engines in order and returns the first organic results. engines=auto tries Google, then Brave, Bing, DuckDuckGo, Yahoo, and Baidu. Omitted gl is us and omitted hl is en. There is no page parameter: the response is always pag… Credit cost: 1 credit per call.

        ``GET / POST /v1/search``

        Args:
            query: Search query.
            engines: Engine order. Default auto tries google, brave, bing, duckduckgo, yahoo, then baidu. A comma-separated list is followed as given. ddg and duck mean duckduckgo. Unknown names are ignored.
            gl: Country code. Defaults to us when omitted. For example us, fr, gb, de.
            hl: Language code. Defaults to en when omitted. For example en, fr, de.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "search",
                {
                    "query": query,
                    "engines": engines,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example google. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/google/search. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse,
            await self._call("stats", {"engine": engine, "path": path}, request_options),
        )

    async def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Retrieve real-time usage statistics and credit balance for your Autom account.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, await self._call("usage", {}, request_options))

    async def yahoo_search(
        self,
        *,
        query: str,
        page: int | float | None = None,
        gl: str | None = None,
        hl: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Yahoo Search. Query Yahoo via API and retrieve structured organic results with country and language. Credit cost: 1 credit per call.

        ``GET / POST /v1/yahoo/search``

        Args:
            query: Search query sent to Yahoo Search.
            page: Page number. Page 1 is the first page of results.
            gl: Country code, for example us, fr, gb, de, jp.
            hl: Language code, for example en, fr, de, ja, zh.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "yahoo_search",
                {
                    "query": query,
                    "page": page,
                    "gl": gl,
                    "hl": hl,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )
