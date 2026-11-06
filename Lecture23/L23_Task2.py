import asyncio
import aiohttp

URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json()
            return data

async def main():
    posts = await fetch_posts()
 
    filtered_posts = [post for post in posts[:20] if post.get("userId") == 1]
    
    for index, post in enumerate(filtered_posts, start=1):
        print(f"{index}. {post['title']}")

asyncio.run(main())