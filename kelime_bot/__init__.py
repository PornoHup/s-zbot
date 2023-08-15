from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = "16102648"
API_HASH = "378a73e340eb634cf67c8c42bafa9f37"
TOKEN = "6221149617:AAEGewuVcP-P1MTtGPOy4rDMwVEkODzTpLQ" 
USERNAME = "SozTapRobot"
OWNER_ID = "6181182367"

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
)


# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore
