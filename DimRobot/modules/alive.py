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
  TEXT += "ð **I'm Working Properly** \n\n"
  TEXT += f"ð **Oá´¡É´á´Ê : [ððð à¼± ððððððð ð¦ð±](https://t.me/Klyuserbot)** \n\n"
  TEXT += f"ð **LÉªÊÊá´ÊÊ Vá´ÊsÉªá´É´    :** `{telever}` \n\n"
  TEXT += f"ð **Tá´Êá´á´Êá´É´ Vá´ÊsÉªá´É´   :** `{tlhver}` \n\n"
  TEXT += f"ð **PÊÊá´É¢Êá´á´ Vá´ÊsÉªá´É´ :** `{pyrover}` \n\n"
  TEXT += f"ð **DimRá´Êá´á´ Vá´ÊsÉªá´É´ :** `{yinzver}` \n\n"
  TEXT += "**Thanks For Adding Me Here â¨**"
  BUTTON = [[Button.url("Help", "https://t.me/DimRobot?start=help"), Button.url("Support", "https://t.me/suportNande")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
