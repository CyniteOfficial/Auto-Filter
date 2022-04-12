from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**Made by @The_obanai_bot**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("Add Link", url="https://t.me/telegram")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    user_id = message.from_user.id
    m = await message.reply_text("ᴘʀᴏᴄᴇssɪɴɢ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
