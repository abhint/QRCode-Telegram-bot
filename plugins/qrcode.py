#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


import os
from pyrogram import Client,Filters
from telegraph import upload_file
import pyqrcode 
import png 


@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        
        chat_id=message.chat.id,
        text=f"<b>Hey {message.from_user.first_name},\nThis is a QR code generator bot by @thankappan369</b>",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )
    
@Client.on_message(Filters.text & Filters.private)
async def qrcode(client, message):
    qr = await client.send_message(
        chat_id=message.chat.id,
        text=f"Making your QR Code... 😁",
        reply_to_message_id=message.message_id  
    )
    s = str(message.text)
    qrname = str(message.from_user.id)
    qrcode = pyqrcode.create(s)
    qrcode.png(qrname + '.png', scale = 6) 
    img = qrname + '.png'
    await qr.edit_text("Uploading... ⏫")
    try:
        response = upload_file(img)
    except Exception as error:
        await qr.edit_text(f"something is went wrong\n{error} \ncontact admin @thankappan369")
        return
    
    await qr.edit_text(f"https://telegra.ph{response[0]}")

    try:
        os.remove(img)
    except Exception as error:
        print('Somting is {error}')
         
