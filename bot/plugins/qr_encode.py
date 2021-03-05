#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


import os
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pyqrcode
from messages import Message
from bot.plugins.display.display_progress import progress


@Client.on_message(filters.text & filters.private)
async def qr_encode(client, message):
    qr = await client.send_message(
        chat_id=message.chat.id,
        text="Making your QR Code... 😁",
        reply_to_message_id=message.message_id
    )
    s = str(message.text)
    qrname = str(message.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale=6)
    img = qrname + '.png'
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"{Message.error}")
        return
    try:
        await message.reply_photo(
            photo=img,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')]]),
            progress=progress,
            progress_args=("Trying to Uploading....", qr)
        )

    except Exception as error:
        print(error)
    try:
        os.remove(img)
    except Exception as error:
        print('Something is {error}')
