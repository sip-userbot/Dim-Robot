import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from DimRobot.events import register
from DimRobot import telethn as tbot

Dimver = "2.0.22"
PHOTO = "https://telegra.ph/file/fa34c7c1016aae47a6354.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm DIM Robot.** \n\n"
    TEXT += "🍁 **I'm Working Properly** \n\n"
    TEXT += f"🍁 **Oᴡɴᴇʀ : [𝐊𝐋𝐘 ༱ 𝐇𝐀𝐍𝐃𝐁𝐄𝐀 🇦🇱](https://t.me/Klyuserbot)** \n\n"
    TEXT += f"🍁 **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ    :** `{telever}` \n\n"
    TEXT += f"🍁 **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ   :** `{tlhver}` \n\n"
    TEXT += f"🍁 **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
    TEXT += f"🍁 **DimRᴏʙᴏᴛ Vᴇʀsɪᴏɴ :** `{yinzver}` \n\n"
    TEXT += "**Thanks For Adding Me Here ✨**"
    BUTTON = [
        [
            Button.url("Help", "https://t.me/DimRobot?start=help"),
            Button.url("Support", "https://t.me/suportNande"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
