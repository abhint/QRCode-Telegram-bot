#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
plugins = dict(
        root="plugins"
    )
bot = Client(
    "QR CODE BOT",
    bot_token = 'Your Bot Token',
    api_id = Your App ID , 
    api_hash = 'yor api_hash',
    plugins = plugins
)
bot.run()