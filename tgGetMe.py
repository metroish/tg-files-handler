import asyncio
from pyrogram import Client

api_id = xxx
api_hash = xxx


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
