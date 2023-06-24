from pyrogram import filters
from HackBot import app 
from HackBot.Config import START_PIC
from HB import START_TEXT,START_BUTTON,HACK_MODS,HACK_TEXT,ABOUT_TEXT
from pyrogram.types import CallbackQuery


@app.on_message(filters.command("start") & filters.private)
async def _start(_, message):
    user = message.from_user.mention
    bot = (await _.get_me()).mention 
    await message.reply_photo(
       photo = START_PIC,
       caption = START_TEXT.format(user)
       reply_markup = START_BUTTON) 


@app.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


@app.on_callback_query(filters.regex("about_me"))
async def aboutme_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(ABOUT_TEXT
              reply_markup = START_BUTTON) 

@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 
