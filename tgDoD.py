import os
import sys
import asyncio
import uvloop
from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo, Message

api_id = xxx 
api_hash = xxx

path='/mnt/d/Upload/target'
keyword = ''

# python tgDoD.py keyword
if len(sys.argv) == 2:
	keyword = sys.argv[1]

def callback(current, total):
    print('Status', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

async def main():
	app = Client("my_account", api_id, api_hash)
	async with app:
		count = await app.search_messages_count("me", keyword)
		print(str(count) + ' msg matched')
		async for msg in app.search_messages("me", query=keyword, limit=count):
				print(msg)
				print(type(msg))
				print('caption = ' + (msg.caption if msg.caption else ''))
				if str(msg.media) == "MessageMediaType.DOCUMENT":
					print('file_name = ' + (msg.document.file_name if msg.document.file_name else ''))
				if str(msg.media) == "MessageMediaType.VIDEO":
					print('file_name = ' + (msg.video.file_name if msg.video.file_name else ''))
				action = input('down/del?')
				if action == 'down':
					await app.download_media(msg, file_name="/mnt/d/Download/", progress=callback)
				elif action == 'del':
					await app.delete_messages("me", msg.id)
				else:
					print('no action.')

uvloop.install()
asyncio.run(main())
