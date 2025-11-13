#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25058583"))
API_HASH = environ.get("API_HASH", "8caa296e93bfd29cacd9d83b242979cc")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "7547625729"))
CREDIT = environ.get("CREDIT", "@ONLY_UPSC_STUDENTSbot")
LOG_GROUP_ID = "-1002940189298"

TOTAL_USER = os.environ.get('TOTAL_USERS', '7547625729,8043050507').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7547625729,8043050507').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set




