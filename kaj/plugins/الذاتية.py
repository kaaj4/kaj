from Superthon import Superthon
from telethon import events
from os import remove

@Superthon.ar_cmd(pattern="(سحب|ذاتية)")
async def datea(event):
    await event.delete()
    scertpic = await event.get_reply_message()
    downloadSuperthon = await scertpic.download_media()
    send = await Superthon.send_file("me", downloadSuperthon)
    remove(downloadSuperthon)
