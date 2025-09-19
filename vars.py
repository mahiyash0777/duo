#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24201237"))
API_HASH = environ.get("API_HASH", "fc82db3f86816844f36abd55bf218b12")
BOT_TOKEN = environ.get("BOT_TOKEN", "7718886627:AAFq__5bZYBiD195qM13iIEb2nCC-q7v3C0")

OWNER = int(environ.get("OWNER", "7547625729"))
CREDIT = environ.get("CREDIT", "𝐒нɑᎥ𝚝ɑη")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7547625729').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7547625729').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set





