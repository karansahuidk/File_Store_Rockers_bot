#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26525323"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a0b7314d9392d1ebda5b62e649a12e91")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002356487898"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1014472611"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://idkfile:idkfile9@cluster0.pvp8h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "699199905e9fa412822d6cdd4e84ba9ad552e78b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_download_tutorial_idk/2")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002442935049"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
import os

START_MSG = os.environ.get("START_MESSAGE", """<b><a href="https://t.me/+nEbKSjDbtEc1ODE1">🍿 𝐎𝐓𝐓 𝐌𝐨𝐯𝐢𝐞 🍿</a><a href="https://t.me/MOVIEX_BACKUP1">🎞 𝐀𝐋𝐋 𝐌𝐎𝐕𝐈𝐄 🎞</a>

                   <a href="https://t.me/+tPrmTQQUT2BkMWRl">🔞 𝐚𝐝𝐮𝐥𝐭 𝐯𝐢𝐝𝐞𝐨 🔞</a>

⚠️ MADE BY @MOVIEX_BACKUP1©️</b>""")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1014472611").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b> You need to join in my Channel/Group and subscribe my youtube channel to use me</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", """{filename}\n\n<a href="t.me/+y4Yfxe221o5iZjQ9">🔞 𝐚𝐝𝐮𝐥𝐭 𝐯𝐢𝐝𝐞𝐨 🔞</a>\n\n<a href="t.me/+D7L-rX9lKA43MGRl">🍿 𝐎𝐓𝐓 𝐌𝐨𝐯𝐢𝐞 🍿</a>\n\n<a href="t.me/+MkmB-unfQk02YTU1">🎞 𝐀𝐋𝐋 𝐌𝐎𝐕𝐈𝐄 🎞</a>""")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = """hello"""

ADMINS.append(OWNER_ID)
ADMINS.append(1014472611)

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
