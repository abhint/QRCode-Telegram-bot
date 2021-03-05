import pyrogram
from pyrogram import Client
from plugins.commands import start, help, about

@Client.on_callback_query()
async def cb_handler(bot, update):
      if "home" in update.data:
        await update.message.delete()
        await start(bot, update.message)
      if "help" in update.data:
        await update.message.delete()
        await help(bot, update.message)
      if "about" in update.data:
        await update.message.delete()
        await about(bot, update.message)
      if "close" in update.data:
        await update.message.delete()
