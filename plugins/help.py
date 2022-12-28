# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Pesquisa no YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, message):
    await message.reply(
        "Este bot pode procurar vídeos do YouTube e baixar vídeos do YouTube, listas de reprodução e muito mais. Use os métodos abaixo para fazer isso\n\n"
        "◉ Procurar vídeos - <i>Usar o modo inline</i>\n"
        "◉ Baixar vídeos - <i>Envie qualquer link de um vídeo do Youtube e selecione uma qualidade</i>\n"
        "◉ Baixar vídeos da lista de reprodução - <i>Enviar qualquer link de uma lista de reprodução do YouTube</i>\n\nIsso é bastante simples. ||Aproveite!!||",
        reply_markup=BUTTONS
    )
