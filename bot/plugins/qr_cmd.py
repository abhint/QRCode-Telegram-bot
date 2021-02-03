from pyrogram import Client, filters
from messages import Msg

@Client.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.start}{Msg.source}",
        reply_to_message_id=message.message_id,
    )

@Client.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(  
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.help}{Msg.source}",
        reply_to_message_id=message.message_id,
    )
