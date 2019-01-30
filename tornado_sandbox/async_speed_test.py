"""
this script based on https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio
Running this script with sync tornado server:
    49.880396, 52

Running this script with async tornado server:
    48.7, 52.8
No difference: ???
"""
import aiohttp
import asyncio
import numpy as np
import requests
import time


async def get_prediction(session, i):
    async with session.post("http://localhost:8888/api/v0/house_value",
            json={"row_index": int(i)}) as response:
         return await response.json()

async def main(N):
    indexes = np.random.randint(low=0, high=20000, size=N)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in indexes:
            tasks.append(get_prediction(session, i))
        predictions = await asyncio.gather(*tasks)


if __name__ == '__main__':
    N = 100
    tic = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(N=N))
    toc = time.perf_counter()
    print("It took %f seconds to do %d requests" % (toc-tic, N))
