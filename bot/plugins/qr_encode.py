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
async def qr_encode(bot, update):
    qr = await bot.send_message(
        chat_id=update.chat.id,
        text="Making your QR Code... 😁",
        reply_to_message_id=update.message_id
    )
    s = str(update.text)
    qrname = str(update.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale=6)
    img = qrname + '.png'
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"{update.error}")
        return
    try:
        await update.reply_photo(
            photo=img,
            caption="<b>Made by @FayasNoushad</b>",
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
