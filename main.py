#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
from ev import ev_data
plugins = dict(root="plugins")
bot = Client(
    "QR CODE BOT",
    bot_token = ev_data.BOT_TOKEN,
    api_id = ev_data.API_ID , 
    api_hash = ev_data.API_HASH,
    plugins = plugins
)
bot.run()