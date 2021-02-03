#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
from env import EnvData

bot = Client(
    "QR CODE BOT",
    bot_token=EnvData.BOT_TOKEN,
    api_id=EnvData.API_ID,
    api_hash=EnvData.API_HASH,
    plugins={
        "root": "bot/plugins"
        },
    parse_mode="html"
)
bot.run()
