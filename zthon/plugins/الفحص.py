import random
import re
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from hunthon import StartTime, sarub, sarversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import saralive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


@sarub.sar_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    sarevent = await edit_or_reply(event, "**⛥ ⤻ انتـظࢪ جـاࢪي فـحص بـ ـوت TEᑭTᕼOᑎ الخـاص بـِك   ۦ**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "☼ ⤶"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** ☼ TEᑭTᕼOᑎ ᗯOᖇKՏ ՏᑌᑕᑕEՏՏᖴᑌᒪᒪY ‌‌‏𓅓 . **"
    sar_IMG = gvarstatus("ALIVE_PIC")
    sar_caption = gvarstatus("ALIVE_TEMPLATE") or sar_temp
    caption = sar_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        zdver=sarversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if sar_IMG:
        sar = [x for x in sar_IMG.split()]
        PIC = random.choice(sar)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await sarevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                sarevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ⪼  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            sarevent,
            caption,
        )


sar_temp = """{ALIVE_TEXT}
———————⛥ ———————
**{Z_EMOJI} َTEᒪETᕼOᑎ 𓋪** `{telever}`
**{Z_EMOJI} ᕼᑌᑎTᕼOᑎ 𓋪** `{zdver}`
**{Z_EMOJI} َᑭYTᕼOᑎ 𓋪** `{pyver}`
**{Z_EMOJI} ᑌᑭTIᗰE 𓋪** `{uptime}`
**{Z_EMOJI} OᗯᑎEᖇ 𓋪** {mention}"""


@sarub.sar_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
    info={
        "header": "- لـ التحـقق مـن أن البـوت يعمـل بنجـاح .. بخـاصيـة الانـلايـن ✓",
        "الاسـتخـدام": [
            "{tr}الفحص",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "☼ ⤶"
    sar_caption = "** ☼ ᕼᑌᑎTᕼOᑎ ᗯOᖇKՏ ՏᑌᑕᑕEՏՏᖴᑌᒪᒪY ‌‌‏𓅓 . **\n"
    sar_caption += f"**{Z_EMOJI} َTEᒪETᕼOᑎ 𓋪** `{version.__version__}\n`"
    sar_caption += f"**{Z_EMOJI} ᕼᑌᑎTᕼOᑎ 𓋪 :** `{sarversion}`\n"
    sar_caption += f"**{Z_EMOJI} َᑭYTᕼOᑎ 𓋪** `{python_version()}\n`"
    sar_caption += f"**{Z_EMOJI} OᗯᑎEᖇ 𓋪** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, sar_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@sarub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await saralive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
