"""Use the asyncio client."""

import asyncio

from autom import AsyncAutomClient


async def main() -> None:
    async with AsyncAutomClient() as client:  # reads AUTOM_API_KEY
        response = await client.google_search(query="web scraping api")
        print(response.data)


asyncio.run(main())
