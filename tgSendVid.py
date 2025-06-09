import os
import sys
import asyncio
import uvloop
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram import Client
from pyrogram.types import InputMediaPhoto, InputMediaVideo

api_id = xxx
api_hash = xxx

path='/mnt/d/Upload/target'
caption_input = ''

# python tgSendFile.py caption
if len(sys.argv) == 2:
	caption_input = sys.argv[1]

def callback(current, total):
    print('Status', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

async def main():
	app = Client("my_account", api_id, api_hash)
	async with app:
		for file_list in os.listdir(path):
			file = os.path.join(path, file_list)
			if os.path.isfile(file):
				file_name, file_ext = os.path.splitext(file)
				if file_ext.lower() == '.mp4':
					md = extractMetadata(createParser(file))
					width = md.get('width')
					height = md.get('height')
					duration = md.get('duration').seconds
					thumb = os.path.join(path, file_name + '.jpg')
					print('start to send file:', file)
					await app.send_video("me", file, width=width, height=height, duration=duration, thumb=thumb, caption=caption_input, progress=callback)

uvloop.install()
asyncio.run(main())
