from pynigger import Nigger
from pynigger.plugins.nigger import HOME_BUTTON
from pyrogram.types import InlineKeyboardMarkup
from pynigger.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY


@Nigger.cmd("about", description="About the bot", private_only=True)
async def about_func(bot, msg):
    try:
        if not module.ABOUT:
            Nigger.log(LOADED_BUT_EMPTY.format("about", "about"), "warn")
            return
        text = await replace(module.ABOUT, msg, bot)
        if await send_buttons():
            await msg.react(text,
                            reply_markup=InlineKeyboardMarkup(HOME_BUTTON))
        else:
            await msg.react(text)
    except AttributeError:
        pass
