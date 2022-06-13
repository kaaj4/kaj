import os

BIO = os.environ.get("BIO", None)
TZ = os.environ.get("TZ", "Asia/Baghdad")
OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
