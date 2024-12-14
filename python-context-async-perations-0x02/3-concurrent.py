import asyncio
import aiosqlite


async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
       async with db.execute("SELECT * FROM users LIMIT 10") as cursor:
           rows = []
           async for row in cursor:
               rows.append(row)
           return rows


async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40 LIMIT 10") as cursor:
           rows = []
           async for row in cursor:
               rows.append(row)
           return rows


async def fetch_concurrently():
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print(results)


if __name__ == '__main__':
    asyncio.run(fetch_concurrently())