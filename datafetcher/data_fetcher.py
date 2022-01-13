import aiohttp
from data.config import big_url,sec_url,vid_url,test_url
async def big():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(big_url) as res:
            return await res.json()

async def sec():
    async with aiohttp.ClientSession() as session:
        async with session.get(sec_url) as result:
            return await result.json()

async def vid():
    async with aiohttp.ClientSession() as session:
        async with session.get(vid_url) as result:
            return await result.json()

async def tests():
    async with aiohttp.ClientSession() as session:
        async with session.get(test_url) as result:
            return await result.json()

async def test(a):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:8000/test/big/{a}') as result:
            return await result.json()