#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25058583"))
API_HASH = environ.get("API_HASH", "8caa296e93bfd29cacd9d83b242979cc")
BOT_TOKEN = environ.get("BOT_TOKEN", "8490510367:AAFmP-ISuFx4ForE-8Q-E1d2SDGsYbjOeXA")

OWNER = int(environ.get("OWNER", "7547625729"))
CREDIT = environ.get("CREDIT", "𝐒ɑη𝐣ɑʏ")
LOG_GROUP_ID = "-1002940189298"

TOTAL_USER = os.environ.get('TOTAL_USERS', '1095085665,7547625729,8365513163').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1095085665,7547625729,8365513163').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



