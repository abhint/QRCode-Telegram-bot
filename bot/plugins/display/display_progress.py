#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

async def progress(current, total, up_msg, message):
    try:
        await message.edit(
            text=f"{up_msg} {current * 100 / total:.1f}%"
        )
    except:
        pass
