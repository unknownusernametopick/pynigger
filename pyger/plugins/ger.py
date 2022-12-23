from pyrogram.types import InlineKeyboardButton


START = """
Hey {user}

Welcome to {bot}

I can {1}
Use below buttons to learn more.

By @NNGerBots
"""

HELP = """
{1}

✨ **Available Commands** ✨

{commands}
"""

ABOUT = """
**About This Bot** 

A telegram bot to {1}{2}

Library : [Pyger](https://github.com/unknownusernametopick/pyger)

Language : [Python](www.python.org)

Developer : @GerProgrammer
"""

HOME_BUTTON = [
    [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
]

MAIN_BUTTONS = [
    [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/NNGerBots/7")],
    [
        InlineKeyboardButton("How to Use ❔", callback_data="help"),
        InlineKeyboardButton("🎪 About 🎪", callback_data="about")
    ],
    [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/NNGerBots")],
]
