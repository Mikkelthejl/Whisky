import aiohttp
import asyncio
from filehandling import Filehandler


    

async def main():
    list = Filehandler()
    await list.initialize()

if __name__ == "__main__":
    asyncio.run(main())