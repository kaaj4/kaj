import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from kaj import kaj, LOGGER
from telethon.tl.functions.channels import JoinChannelRequest
from kaj.plugins import *
async def saves():
    try:
        os.environ["STRING_SESSION"] = "**@kaj**"
    except Exception as e:
        print(str(e))
    try:
        await kaj(JoinChannelRequest("@iqthon"))
    except BaseException:
        pass
def load_plugins(plugin_name):
    path = Path(f"kaj/plugins/{plugin_name}.py")
    name = "kaj.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["kaj.plugins." + plugin_name] = load
path = "kaj/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
kaj.start()
kaj.loop.create_task(saves())
print("- تم بنجاح تنصيب سورس سورس كاج  @kaj")
kaj.run_until_disconnected()
