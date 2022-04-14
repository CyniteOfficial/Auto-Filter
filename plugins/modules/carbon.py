from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**𝙼𝙰𝙳𝙴 𝙱𝚈 [𝙰𝙹𝙰𝚇](https://t.me/Devil0Bot_Bot)**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url="https://t.me/OpusTechz")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝚃𝙴𝚇𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙲𝙰𝚁𝙱𝙾𝙽.**"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝚃𝙴𝚇𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙲𝙰𝚁𝙱𝙾𝙽.**"
        )
    user_id = message.from_user.id
    m = await message.reply_text("**𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝙲𝙰𝚁𝙱𝙾𝙽...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙲𝙰𝚁𝙱𝙾𝙽...**")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
