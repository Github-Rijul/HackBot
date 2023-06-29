import logging
from HackBot.Config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(level=logging.INFO)

app = Client(
    "Legend",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN)
