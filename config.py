#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6871953339:AAEqYg-a86K-qfGq1ZS7LkXaHvpolvZTa7E")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21942125"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6d412af77ce89f5bb1ed8971589d61b5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001886911325"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6331847574"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://strong:strong@cluster0.ix7usa3.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "028dcc84c348788150cdbc48331a813bf7a8d257")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_open_link_rockersbot/19")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001910410959"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
import os

START_MSG = os.environ.get("START_MESSAGE", """<b><a href="t.me/+D7L-rX9lKA43MGRl">🍿 𝐎𝐓𝐓 𝐌𝐨𝐯𝐢𝐞 🍿</a><a href="t.me/+MkmB-unfQk02YTU1">🎞 𝐀𝐋𝐋 𝐌𝐎𝐕𝐈𝐄 🎞</a>

                   <a href="t.me/+y4Yfxe221o5iZjQ9">🔞 𝐚𝐝𝐮𝐥𝐭 𝐯𝐢𝐝𝐞𝐨 🔞</a>

⚠️ MADE BY @ROCKERSBACKUP ©️</b>""")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6331847574").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>You need to join in my Channel/Group and subscribe my youtube channel to use me\n\nSubscribe :- https://youtube.com/@jnentertainment.?si=GRyKp5kUhDtP3Ssu</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", """{filename}\n\n<a href="t.me/+y4Yfxe221o5iZjQ9">🔞 𝐚𝐝𝐮𝐥𝐭 𝐯𝐢𝐝𝐞𝐨 🔞</a>\n\n<a href="t.me/+D7L-rX9lKA43MGRl">🍿 𝐎𝐓𝐓 𝐌𝐨𝐯𝐢𝐞 🍿</a>\n\n<a href="t.me/+MkmB-unfQk02YTU1">🎞 𝐀𝐋𝐋 𝐌𝐎𝐕𝐈𝐄 🎞</a>""")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ Aske UR Movies Here :- https://t.me/Rockers_ott_movie_link_bot"

ADMINS.append(OWNER_ID)
ADMINS.append(6331847574)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
