# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/abhint
# (c) Abhijith N T 
# Thank you https://github.com/pyrogram/pyrogram 


from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

bot = Client(
    "QR CODE BOT",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        "root": "bot/plugins"
    },
    parse_mode="html"
)
bot.run()
