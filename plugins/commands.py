import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.add import add_user_to_database

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
