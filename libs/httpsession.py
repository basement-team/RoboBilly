import socket
import asyncio

from aiohttp import AsyncResolver, ClientSession, TCPConnector

try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except:
    pass

http_session = ClientSession(
    connector=TCPConnector(resolver=AsyncResolver(), family=socket.AF_INET)
)

async def close_session():
    await http_session.close()
