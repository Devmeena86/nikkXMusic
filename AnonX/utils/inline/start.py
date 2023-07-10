from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ  ᴍᴇ  ᴍᴏɪ  ʙᴀʙy",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
          
            )
        ],
        [
            InlineKeyboardButton(
                text="💝 Gʀᴏᴜᴩ  Sᴇᴛᴛɪɴɢ 💝", callback_data="settings_helper"
            ),           
     
            InlineKeyboardButton(
                text="❤️‍🔥 Cʜᴀᴛᴛɪɴɢ ❤️‍🔥", url=f"https://t.me/II_VNND_WORLD_II"
           
            ),
        ],
        [
            InlineKeyboardButton(
                text="💘 Nᴇᴛᴡᴏʀᴋ 💘", url=f"https://t.me/NIDHI_NETWORKS"
           
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ  ᴍᴇ  ᴍᴏɪ  ʙᴀʙy",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 Hᴇʟᴩ & Cᴏᴍᴍᴀɴᴅꜱ 🦋", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Cʜᴀᴛᴛɪɴɢ ❤️‍🔥", url=f"https://t.me/II_VNND_WORLD_II"
            ),
            InlineKeyboardButton(
                text="💔 Dᴇᴠᴇʟᴏᴩᴇʀ 💔", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🩹 Sᴏᴜʀᴄᴇ ❤️‍🩹" , url=f"https://te.legra.ph/file/ebee76577947b83208dac.jpg"
             
            )
        ],
     ]
    return buttons
