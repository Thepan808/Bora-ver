# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 4954361))
    API_HASH = os.environ.get("API_HASH", "43a786a8548a30f9d6887e36d53c0e64")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5612901649:AAHm5GgcpXuXs57zRGR4JzzbB94ouYU8IiU")
