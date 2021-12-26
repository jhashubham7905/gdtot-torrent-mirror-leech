# Remove this line before deploying
=True
# REQUIRED CONFIG
BOT_TOKEN = "1898608432:AAEkSICsLzzUTTwW_EkRN12Xb2lIrnKmPO8"
GDRIVE_FOLDER_ID = "0AL2RQngURNxRUk9PVA"
OWNER_ID = 1167961858
DOWNLOAD_DIR = "/usr/src/app/downloads"
DOWNLOAD_STATUS_UPDATE_INTERVAL = 5
AUTO_DELETE_MESSAGE_DURATION = 10
IS_TEAM_DRIVE = "True"
TELEGRAM_API = 1206485
TELEGRAM_HASH = "2897112fa3a92f6fcc61c73d6e2904c9"
BASE_URL_OF_BOT = "https://torrentbullbot-2-82-1.herokuapp.com"  # Web Link, Required for (Heroku) to avoid sleep or use worker if you don't want to use web (selection)
# OPTIONAL CONFIG
DATABASE_URL = "postgres://bhzelzhl:TlJl7qijXtZVZpJQpgccsGpuet7tTUct@john.db.elephantsql.com/bhzelzhl"
AUTHORIZED_CHATS = "-1001558257521"  # Split by space
SUDO_USERS = "1167961858"  # Split by space
IGNORE_PENDING_REQUESTS = "False"
USE_SERVICE_ACCOUNTS = "True"
INDEX_URL = "https://new-drive-torrent-bullmovies.bullmovies2.workers.dev/0:/"
STATUS_LIMIT = "4"  # Recommended limit is 4
UPTOBOX_TOKEN = ""
MEGA_API_KEY = ""
MEGA_EMAIL_ID = ""
MEGA_PASSWORD = ""
BLOCK_MEGA_FOLDER = "False"
BLOCK_MEGA_LINKS = "False"
STOP_DUPLICATE = "True"
SHORTENER = ""
SHORTENER_API = ""
SEARCH_API_LINK = ""
UPSTREAM_REPO = ""
# Leech
TG_SPLIT_SIZE = ""  # leave it empty for max size (2GB), or add size in bytes
AS_DOCUMENT = "False"
EQUAL_SPLITS = "True"
CUSTOM_FILENAME = ""
# qBittorrent
IS_VPS = ""  # Don't set this to True even if you're using VPS, unless facing error with web server
SERVER_PORT = "80"  # Only For VPS even if IS_VPS is False
WEB_PINCODE = ""
# If you want to use Credentials externally from Index Links, fill these vars with the direct links
# These are optional, if you don't know about them, simply leave them empty
ACCOUNTS_ZIP_URL = ""
TOKEN_PICKLE_URL = ""
MULTI_SEARCH_URL = ""  # You can use gist raw link (remove commit id from the link, like config raw link check Heroku guide)
YT_COOKIES_URL = ""  # You can use gist raw link
NETRC_URL = ""  # You can use gist raw link
# GDTOT COOKIES
PHPSESSID = "bee6sasuocg3b0nbqsp99c2o64"
CRYPT = "RDZMU3hTWHdtRXViOXhoUnFQS280cEFIN3dHUTBiVkdNQzkxSUllV0ZkND0%3D"
# To use limit don't add unit. Default unit is GB.
TORRENT_DIRECT_LIMIT = ""
ZIP_UNZIP_LIMIT = ""
CLONE_LIMIT = ""
MEGA_LIMIT = ""
# View Link button to open file Index Link in browser instead of direct download link
# You can figure out if it's compatible with your Index code or not, open any video from you Index and check if its URL ends with ?a=view, if yes fill True it will work (Compatible with Bhadoo Drive Index)
VIEW_LINK = "True"
# Add more buttons (Three buttons are already added including Drive Link, Index Link, and View Link, you can add extra buttons too, these are optional)
# If you don't know what are below entries, simply leave them empty
BUTTON_FOUR_NAME = ""
BUTTON_FOUR_URL = ""
BUTTON_FIVE_NAME = ""
BUTTON_FIVE_URL = ""
BUTTON_SIX_NAME = ""
BUTTON_SIX_URL = ""
