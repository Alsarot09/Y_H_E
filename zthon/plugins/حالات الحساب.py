import base64
import contextlib
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from . import zedub

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _format, get_user_from_event
from ..sql_helper import broadcast_sql as sql
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البوت"
LOGS = logging.getLogger(__name__)

zed_BLACKLIST = [
    -1001927413014,
    -1001636220368,
    ]

DEVZ = [
    6275274612,
    6002442759,
    6516959003,
    6091420311,
]
#

ALSAROTPRO_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡 𝗖𝗼𝗻𝗳𝗶𝗴 - أوامـر حـالات الحـساب](t.me/HunerThon) 𓆪\n\n"
    "**⎞➊⎝** `.نائم`\n"
    "**بـ كتابـة أمـر ( .نائم ) سيتم وضع صـورة تدل عـلى أنـك نائـم ووضـع كلمـة نائم بجانــب اســمك**\n"
    "**⎞➋⎝** `.مستيقظ`\n"
    "**يقـوم هـذا الأمـر بإعـادة حسـابك إلـى وضعـه الطبيعـي**\n"
    "**⎞➌⎝** `.اوفلاين`\n"
    "**بـ كتـابـة هـذا الأمـر سيتـم وضـع صـورة أوفلاين وسيتـم وضـع كلـمـة أوفلاين بجانـب اســمـك**\n"
    "**⎞➍⎝** `.اونلاين`\n"
    "**يقـوم هـذا الأمـر بإعـادة حسـابك إلـى وضعـه الطبيعـي**\n"
    "\n 𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗛𝗨𝗡𝗧𝗘𝗥𝗧𝗛𝗢𝗡](t.me/HunerThon) 𓆪"
)


@zedub.zed_cmd(pattern="حالات الحساب")
async def cmd(ALSAROT):
    await edit_or_reply(ALSAROT, ALSAROTPRO_cmd)

