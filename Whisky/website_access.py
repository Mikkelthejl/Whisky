import asyncio, aiohttp, json, requests

class access:
    async def access():
        async with aiohttp.ClientSession() as session:
            website = Website("")
            for element in website.sites:
                page = f'{website.site}{element}'
                site_response = await fetcher.find_items(session,page)