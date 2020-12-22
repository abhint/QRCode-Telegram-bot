from pyrogram import Client,Filters
from messages import msg

@Client.on_message(Filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{msg.start}{msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )
@Client.on_message(Filters.command(["help","h"]))
async def help(client, message):
    await client.send_message(  
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{msg.help}{msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode = "html" 
    )