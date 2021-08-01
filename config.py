import os
from dotenv import load_dotenv
load_dotenv()

# from @botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# from https://my.telegram.org/apps
API_ID = int(os.environ.get("API_ID"))
# from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH")
