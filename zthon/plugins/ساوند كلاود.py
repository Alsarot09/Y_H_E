import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from hunthon import sarub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


@sarub.sar_cmd(
    pattern="ساوند(?:\s|$)([\s\S]*)",
    command=("ساوند", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلود عبر الرابـط",
        "الاستـخـدام": "{tr}ساوند بالـرد ع رابـط",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(event, "**╮ ❐ جـارِ التحميـل من سـاوند كـلاود انتظـر قليلاً  ▬▭... 𓅫╰**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت @TlkTokDownloaderbot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@sarub.sar_cmd(
    pattern="كلود ([\s\S]*)",
    command=("كلود", plugin_category),
    info={
        "header": "لتحميل الاغاني من ساوند كلود عبر الرابـط",
        "الاستـخـدام": "{tr}كلود + رابط",
    },
)
async def sar(event):
    if event.fwd_from:
        return
    sarr = event.pattern_match.group(1)
    alsarot = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, sarr)
    await tap[0].click(event.chat_id)
    await event.delete()
