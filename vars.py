#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26375665"))
API_HASH = environ.get("API_HASH", "568839157ce65f4d3a91647f022b6737")
BOT_TOKEN = environ.get("BOT_TOKEN", "8380810929:AAEltCJe5zg4SE0lYav3NcSx02pTU8wMsC8")

OWNER = int(environ.get("OWNER", "6834250190"))
CREDIT = environ.get("CREDIT", "𝐒нɑᎥ𝚝ɑη")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6834250190,6312355641').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6834250190,6312355641').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
