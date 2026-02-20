import re
from os import environ

# -------------------------
# Helper
# -------------------------
def str_to_bool(val, default=False):
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "on")

# =========================================================
# 🤖 BOT BASIC INFORMATION
# =========================================================
API_ID = int(environ.get("API_ID", "29904834"))
API_HASH = environ.get("API_HASH", "8b4fd9ef578af114502feeafa2d31938")
BOT_TOKEN = environ.get("BOT_TOKEN", "8206083172:AAGFozLcAUF-OlzLb_vtyE24rGGZJsr70jE")
PORT = int(environ.get("PORT", "8080"))
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
OWNER_USERNAME = environ.get("OWNER_USERNAME", "ak_admin_v2Bot")

# =========================================================
# 💾 DATABASE CONFIGURATION
# =========================================================
DB_URL = environ.get("DATABASE_URI", "mongodb+srv://roxiw19528:roxiw19528@cluster0.vl508y4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DATABASE_NAME", "ak_admin_v2Bot")

# =========================================================
# 📢 CHANNELS & ADMINS
# =========================================================
ADMINS = int(environ.get("ADMINS", "7120801813"))

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003653363264"))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", "-1003653363264"))
VERIFIED_LOG = int(environ.get("VERIFIED_LOG", "-1003653363264"))

POST_CHANNEL = int(environ.get("POST_CHANNEL", "-1003755931989"))
VIDEO_CHANNEL = int(environ.get("VIDEO_CHANNEL", "-1003734578814"))
BRAZZER_CHANNEL = int(environ.get("BRAZZER_CHANNEL", "-1003635143381"))

# Auth channels list
auth_channel_str = environ.get("AUTH_CHANNEL", "-1003755931989")
AUTH_CHANNEL = [int(x) for x in auth_channel_str.split() if x.strip().lstrip("-").isdigit()]

# =========================================================
# ⚙️ FEATURES & TOGGLES  (FIXED)
# =========================================================
FSUB = str_to_bool(environ.get("FSUB"), True)
IS_VERIFY = str_to_bool(environ.get("IS_VERIFY"), True)
POST_SHORTLINK = str_to_bool(environ.get("POST_SHORTLINK"), False)
SEND_POST = str_to_bool(environ.get("SEND_POST"), False)
PROTECT_CONTENT = str_to_bool(environ.get("PROTECT_CONTENT"), True)

# =========================================================
# 🔢 LIMITS
# =========================================================
DAILY_LIMIT = int(environ.get("DAILY_LIMIT", "5"))
VERIFICATION_DAILY_LIMIT = int(environ.get("VERIFICATION_DAILY_LIMIT", "5"))
PREMIUM_DAILY_LIMIT = int(environ.get("PREMIUM_DAILY_LIMIT", "50000000000000000"))

# =========================================================
# 🔗 SHORTLINK & VERIFICATION
# =========================================================
SHORTLINK_URL = environ.get("SHORTLINK_URL", "urlbotsot.vercel.app")
SHORTLINK_API = environ.get("SHORTLINK_API", "akashdeveloper")
POST_SHORTLINK_URL = environ.get("POST_SHORTLINK_URL", "")
POST_SHORTLINK_API = environ.get("POST_SHORTLINK_API", "")
VERIFY_EXPIRE = int(environ.get("VERIFY_EXPIRE", "3600"))
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://t.me/BotFileD/2")

# =========================================================
# 💳 PAYMENT SETTINGS
# =========================================================
UPI_ID = environ.get("UPI_ID", "")
QR_CODE_IMAGE = environ.get("QR_CODE_IMAGE", "")

# =========================================================
# 🖼️ IMAGES
# =========================================================
START_PIC = environ.get("START_PIC", "https://i.postimg.cc/nrDy9Vwh/IMG-20260220-150018-186.jpg")
AUTH_PICS = environ.get("AUTH_PICS", "")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://i.postimg.cc/64QVrpKc/IMG-20260220-151644-654.jpg")
NO_IMG = environ.get("NO_IMG", "")

# =========================================================
# 🌐 WEB APP
# =========================================================
WEB_APP_URL = environ.get("WEB_APP_URL", "https://pronwalizonebot-yehg.onrender.com")
