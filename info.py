import re
import os
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = os.environ.get('SESSION', 'Media_search')
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(os.environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(os.environ.get('USE_CAPTION_FILTER', True))

PICS = (os.environ.get(
    'PICS',
    'https://telegra.ph/file/65fe86fc02a73f6fcf0ce.jpg '
    'https://telegra.ph/file/6fa70325813885809a64a.jpg '
    'https://telegra.ph/file/e06afc1e7abbcd8d4213a.jpg '
    'https://telegra.ph/file/3f4040b320d9b7840200a.jpg '
    'https://telegra.ph/file/3950fad740fb8ea894df7.jpg'
)).split()

NOR_IMG = os.environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_VID = os.environ.get("MELCOW_VID", "https://telegra.ph/file/85d361ab4cb6511006022.mp4")
SPELL_IMG = os.environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = os.environ.get('SUBSCRIPTION', 'https://telegra.ph/file/734170f40b8169830d821.jpg')
CODE = os.environ.get('CODE', 'https://telegra.ph/file/72f425007b22d28bd935e.jpg')

# Stream link shortener
STREAM_SITE = os.environ.get('STREAM_SITE', 'ziplinker.net')
STREAM_API = os.environ.get('STREAM_API', 'ae0832f39e24094a0661626a792e6a2b8880e310')
STREAMHTO = os.environ.get('STREAMHTO', 'https://t.me/HowToOpenLinkHP/69')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in os.environ.get('PREMIUM_USER', '').split()]
auth_channel = os.environ.get('AUTH_CHANNEL', '')
auth_grp = os.environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = os.environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = os.environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(os.environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = os.environ.get('DATABASE_URI', "")
DATABASE_NAME = os.environ.get('DATABASE_NAME', "")
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')

# Verify
VERIFY = bool(os.environ.get('VERIFY', False))
HOWTOVERIFY = os.environ.get('HOWTOVERIFY', 'https://t.me/')  # Fixed here

# Others
SHORTLINK_URL = os.environ.get('SHORTLINK_URL', 'instantearn.in')
SHORTLINK_API = os.environ.get('SHORTLINK_API', '1502a197c85d59929d50f1cba1d5e6f967d1e962')
IS_SHORTLINK = bool(os.environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in os.environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = os.environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled(os.environ.get('MAX_BTN', "True"), True)
PORT = os.environ.get("PORT", "8080")
GRP_LNK = os.environ.get('GRP_LNK', 'https://t.me/')
CHNL_LNK = os.environ.get('CHNL_LNK', 'https://t.me/')
TUTORIAL = os.environ.get('TUTORIAL', 'https://t.me/')
IS_TUTORIAL = bool(os.environ.get('IS_TUTORIAL', True))
MSG_ALRT = os.environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴘ')
LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = os.environ.get('SUPPORT_CHAT', 'https://t.me/')
P_TTI_SHOW_OFF = is_enabled(os.environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(os.environ.get('IMDB', "False"), False)
AUTO_FFILTER = is_enabled(os.environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(os.environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(os.environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = os.environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = os.environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = os.environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(os.environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(os.environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = os.environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(os.environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (os.environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(os.environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(os.environ.get('PROTECT_CONTENT', "True"), True)
PUBLIC_FILE_STORE = is_enabled(os.environ.get('PUBLIC_FILE_STORE', "True"), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

# Online Stream and Download
NO_PORT = bool(os.environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = os.environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(os.environ.get('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(os.environ.get('FQDN', BIND_ADRESS)) if not ON_HEROKU or os.environ.get('FQDN') else APP_NAME + '.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(os.environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(os.environ.get('WORKERS', '4'))
SESSION_NAME = str(os.environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(os.environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "1200"))

if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = str(os.environ.get('APP_NAME'))
else:
    ON_HEROKU = False

HAS_SSL = bool(os.environ.get('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# Premium logs
PREMIUM_LOGS = int(os.environ.get('PREMIUM_LOGS', ''))

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing IMDb details for your queries.\n" if IMDB else "IMDb Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and file size will be shown in a single button.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found.\n")
LOG_STR += ("Long IMDb storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled.\n")
LOG_STR += ("Spell Check Mode Is Enabled.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled.\n")
LOG_STR += (f"MAX_LIST_ELM Found, limited to {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full List will be shown.\n")
LOG_STR += f"Your current IMDb template is {IMDB_TEMPLATE}"
