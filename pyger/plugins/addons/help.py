from pyger import Ger
from pyger.plugins.ger import HOME_BUTTON
from pyrogram.types import InlineKeyboardMarkup
from pyger.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY, replace_commands


@Ger.cmd('help', description="How to use the bot?", private_only=True)
async def help_func(bot: Ger, msg):
    try:
        if not module.HELP:
            Ger.log(LOADED_BUT_EMPTY.format("help", "help"), "warn")
            return
        text = str(module.HELP)
        if "{commands}" in text:
            text = await replace_commands(bot, text)
        text = await replace(text, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(HOME_BUTTON))
        else:
            await msg.react(text)
    except AttributeError:
        pass
