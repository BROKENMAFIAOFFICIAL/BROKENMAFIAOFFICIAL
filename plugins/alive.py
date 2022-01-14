import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/564f5ebbd100278261a03.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ʀᴏᴄᴋᴇʀᴢ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴘᴇʀғᴇᴄᴛ sᴀʟɪᴍ](https://t.me/xmartperson)
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴘᴇʀғᴇᴄᴛ sᴀʟɪᴍ](https://t.me/xmartperson)
┣★ sᴜᴘᴘᴏʀᴛ :  [ᴡᴀʀʙᴏᴛᴢ sᴜᴘᴘᴏʀᴛ](https://t.me/warbotzsupport)
┣★ ᴄʜᴀᴛᴛɪɴɢ : [xᴍᴀʀᴛʏ Cʜᴀᴛ](https://t.me/xmarty_support)
┣★  oᴡɴᴇʀ › : [ᴘᴇʀғᴇᴄᴛ sᴀʟɪᴍ](https://t.me/xmartperson)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ᴘᴇʀғᴇᴄᴛ ᴏᴡɴᴇʀ](https://t.me/xmartperson) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ɴᴅ sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ ❱ ➕", url=f"https://t.me/warbotzsupport")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "sᴀʟɪᴍ"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/564f5ebbd100278261a03.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/warbotzsupport")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/564f5ebbd100278261a03.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://github.com/S780821/Rockerz_Musicplayer")
                ]
            ]
        ),
    )
