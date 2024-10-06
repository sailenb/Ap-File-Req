#(©)NextGenBotz




import os
import logging
from logging.handlers import RotatingFileHandler
from os import environ


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7223208724:AAETLhUUtC5dLskol_xWYz-cpor0Q1cHEzk")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29759992"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "61f150cdca64b2916fa499d107393140")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002216311890"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5787502520"))

#Port
PORT = os.environ.get("PORT", "5151")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://zxbots:zXaBhi2315a@cluster0.lbbygpm.mongodb.net/?retryWrites=true&w=majorit")
DB_NAME = os.environ.get("DATABASE_NAME", "zxbots")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002067949142"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002055777287"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "20"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b><b>👋👋 Hey {first} ! </b>\n\n<b>I'm a File Store Bot🤖...! </b>\n\nI Can <b>Store Private Files</b> in Specified Channel and other users can access Private Files From a Special Link....!\n\n⚡<b>Powered By - </b>@About_Yae_Miko")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5787502520").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join both Channel to use me.\n\nPlease join Both of Channel and Try Again</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(7949270179)

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
   
