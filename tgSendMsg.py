import os
import sys
import asyncio
from pyrogram import Client

api_id = xxx
api_hash = xxx

msg_input = ''
# python tgSendMsg.py msg
if len(sys.argv) == 2:
    msg_input = sys.argv[1]

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", msg_input)


asyncio.run(main())
