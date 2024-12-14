import asyncio
import aiosqlite


async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
       async with db.execute("SELECT * FROM users LIMIT 10") as cursor:
           async for row in cursor:
               print(row)


async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40 LIMIT 10") as cursor:
            async for row in cursor:
               print(row)


async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )


if __name__ == '__main__':
    asyncio.run(fetch_concurrently())