import time, os
from datetime import datetime
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
string = os.environ["STRING_SESSION"]
LOGGER = logging.getLogger(__name__)
StartTime = time.time()
kaj = TelegramClient(StringSession(string), api_id, api_hash)
