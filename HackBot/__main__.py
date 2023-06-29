from HackBot.core.clients import app
from HackBot.plugins import ALL_MODULES

async def start_bot():
  await app.start()  
  for all_module in ALL_MODULES:
        importlib.import_module("HackBot.plugins." + all_module)
