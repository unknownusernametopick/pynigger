from pyger import Ger
try:
    from telegramdb import TelegramDB, DataPack, Member
except ImportError:
    import os
    Ger.log('Installing TelegramDB...')
    os.system('pip3 install TelegramDB==0.2.0')
    from telegramdb import TelegramDB, DataPack, Member
import os
import sys
import traceback
from ..config import ENV
from pyrogram import Client
from ..logger import logger

env = ENV()
DB_SESSION = env.DB_SESSION
DB_CHAT_ID = env.DB_CHAT_ID
API_ID = env.API_ID
API_HASH = env.API_HASH

if not DB_SESSION:
    Ger.log('No DB_SESSION defined. Exiting...', "critical")
    raise SystemExit
userbot = Client(DB_SESSION, api_id=API_ID, api_hash=API_HASH)
userbot.start()

if not DB_CHAT_ID:
    Ger.log("No DB_CHAT_ID found. Creating a chat for database", "warning")
    channel = userbot.create_channel("Pyger Telegram DB")
    Ger.log(f"Telegram DB Channel ID is {channel.id}")
    DB_CHAT_ID = channel.id

if isinstance(DB_CHAT_ID, str) and DB_CHAT_ID[1:].isdigit():
    DB_CHAT_ID = int(DB_CHAT_ID)


sys.stdout = open(os.devnull, 'w')
try:
    Session = TelegramDB(userbot, DB_CHAT_ID, debug=True, logger=logger)
    sys.stdout = sys.__stdout__
except Exception as e:
    sys.stdout = sys.__stdout__
    Ger.log(str(e), "critical")
    Ger.log("Your DB_CHAT_ID is incorrect.", "critical")
    Ger.log(traceback.format_exc(), "critical")
    raise SystemExit
Ger.log("Initializing TelegramDB [Copyright (C) 2022 anonyindian]")
