import os
import sys
import asyncio
import uvloop
from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo

api_id = xxx
api_hash = xxx

path='/mnt/d/Upload/target'
media_list = []
caption_input = ''

# python tgSendGroup.py caption
if len(sys.argv) == 2:
	caption_input = sys.argv[1]

def callback(current, total):
    print('Status', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

for file_list in os.listdir(path):
	file = os.path.join(path, file_list)
	if os.path.isfile(file):
		file_name, file_ext = os.path.splitext(file)
		photo_ext = ['.jpg', '.png', '.jpeg']
		if file_ext.lower() in str(photo_ext):
			media_list.append(InputMediaPhoto(file, caption=caption_input))
		if file_ext.lower() == '.mp4':
			media_list.append(InputMediaVideo(file, caption=caption_input))

async def main():
	app = Client("my_account", api_id, api_hash)
	async with app:
		await app.send_media_group("me", media_list)

uvloop.install()
asyncio.run(main())
