#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
from env import env_data

bot = Client(
    "QR CODE BOT",
    bot_token = env_data.BOT_TOKEN,
    api_id = env_data.API_ID,
    api_hash = env_data.API_HASH,
    plugins = {
        "root":"bot/plugins"
        }
)
bot.run()