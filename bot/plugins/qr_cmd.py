from pyrogram import Client, filters
from messages import (START, SOURCE,HELP)


@Client.on_message(filters.command("start") & filters.private)
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{START}{SOURCE}",
        reply_to_message_id=message.message_id,
    )


@Client.on_message(filters.command(["help", "h"]) & filters.private)
async def help_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{HELP}{SOURCE}",
        reply_to_message_id=message.message_id,
    )
