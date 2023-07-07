from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤣 𝙳𝙴𝚅'𝚂 𝙶𝙵 🤭",
                url=f"https://t.me/Itz_darshaner",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌹 𝙳𝙴𝚅'𝚂  𝙱𝙷𝙰𝙸 🌹",
                url=f"https://t.me/ITZ_NIKK_BABY",
          
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝚂𝙴𝚃𝚃𝙸𝙽𝙶 😂", callback_data="settings_helper"
            )
         ],
         [   
             InlineKeyboardButton(
                text="🔥 𝙳𝙴𝚅'𝚂  𝙵𝚁𝙸𝙴𝙽𝙳 💖", url=f"https://t.me/Mahakal_ki_mahakali"
           
            ),
            InlineKeyboardButton(
                text="🔥 𝙳𝙴𝚅'𝚂  𝙵𝚁𝙸𝙴𝙽𝙳 💖", url=f"https://t.me/ITZ_CANDY_SHARMA"
           
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🤭 𝙰𝙳𝙳  𝙼𝙴  𝙼𝙾𝙸  𝙱𝙰𝙱𝚈 😴",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂 𝙷𝙴𝙻𝙿  𝙰𝙽𝙳  𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 🍂", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💘 𝙲𝙷𝙰𝚃𝚃𝙸𝙽𝙶 💘", url=f"https://t.me/II_VNND_WORLD_II"
            ),
            InlineKeyboardButton(
                text="🔥 𝙵𝙾𝚄𝙽𝙳𝙴𝚁  🙂", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚂𝙾𝚄𝚁𝙲𝙴" , url="https://te.legra.ph/file/ebee76577947b83208dac.jpg"
             
            )
        ],
     ]
    return buttons
