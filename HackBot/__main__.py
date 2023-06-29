import platform

import asyncio
import importlib

from pyrogram import idle
from pyrogram import __version__ as py_version

from HackBot.core.clients import app
from HackBot.plugins import ALL_MODULES
from HackBot import version

async def start_bot():
  await app.start()  
  for all_module in ALL_MODULES:
        importlib.import_module("HackBot.plugins." + all_module)
  print("➖➖➖➖➖➖➖➖➖➖➖➖")
  print(f"🧿 HackBot 🧿[INFO] : Channel Username {ch_username}")
  print(f"🧿 HackBot 🧿[INFO] : Version - {platform.python_version()}")
  print(f"🧿 HackBot 🧿[INFO]: HackBot Version - {version}")
  print(f"🧿 HackBot 🧿[INFO]: Pyrogram Version - {py_version}")
  print("➖➖➖➖➖➖➖➖➖➖➖➖")
  await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
