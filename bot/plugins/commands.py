from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from messages import Message

@Client.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.delete()
    if update.data == "help":
        await update.message.delete()
    if update.data == "close":
        await update.message.delete()

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Message.START_TEXT.format(update.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/FayasNoushad'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/FayasChat'),],
                                           [InlineKeyboardButton('⚜ Help and Informations ⚜', callback_data='help')]]),
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Message.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/FayasNoushad'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/FayasChat'),],
                                           [InlineKeyboardButton('⚜ Back to Home ⚜', callback_data='home')]]),
        reply_to_message_id=update.message_id
    )
