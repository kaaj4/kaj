import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from iqthon import iqthon, LOGGER
from telethon.tl.functions.channels import JoinChannelRequest
from iqthon.plugins import *

async def saves():
    try:
        os.environ["STRING_SESSION"] = "**@IQTHON**"
    except Exception as e:
        print(str(e))
    try:
        await iqthon(JoinChannelRequest("@iqthon"))
    except BaseException:
        pass
    try:
        await iqthon(JoinChannelRequest("@telethonmusic"))
    except BaseException:
        pass

def load_plugins(plugin_name):
    path = Path(f"iqthon/plugins/{plugin_name}.py")
    name = "iqthon.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["iqthon.plugins." + plugin_name] = load

path = "iqthon/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

iqthon.start()

iqthon.loop.create_task(saves())

print("- تم بنجاح تنصيب سورس تليثون  @iqthon")

iqthon.run_until_disconnected()
