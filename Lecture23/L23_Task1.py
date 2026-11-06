import asyncio
import time
import aiohttp
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

start_time_sync = time.time()

sync_results = []
for i in range(1, 11):
  response = requests.get(f"{BASE_URL}/{i}")
  sync_results.append(response.json())

end_time_sync = time.time()
sync_duration = end_time_sync - start_time_sync
print(f"სინქრონულის დრო: {sync_duration:.4f} წამი")

async def fetch(session, url):
  async with session.get(url) as response:
    return await response.json()

async def main_async():
  async with aiohttp.ClientSession() as session:
    tasks = [fetch(session, f"{BASE_URL}/{i}") for i in range(1, 11)]
    return await asyncio.gather(*tasks)

start_time_async = time.time()

async_results = asyncio.run(main_async())

end_time_async = time.time()
async_duration = end_time_async - start_time_async
print(f"ასინქრონულის დრო: {async_duration:.4f} წამი")

time_difference = sync_duration - async_duration

print(f"\nასინქრონულმა ვერსიამ {time_difference:.4f} წამით უფრო სწრაფად იმუშავა")