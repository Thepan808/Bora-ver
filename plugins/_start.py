# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Pesquisa no YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    reply_markup = START_BUTTONS
    await message.reply(
        f"Olá {message.from_user.first_name}!\n\nEste bot pode procurar vídeos do YouTube e baixar vídeos do YouTube, listas de reprodução e muito mais. "
        f"Para pesquisar vídeos, clique no botão abaixo \"🔍Pesquisa no Youtube\" botão. /help para mais informações.", reply_markup=reply_markup)
