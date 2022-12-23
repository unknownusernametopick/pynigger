from pynigger import Nigger
from pynigger.plugins.ger import MAIN_BUTTONS
from pyrogram.types import InlineKeyboardMarkup
from pynigger.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY


@Nigger.cmd('start', description="Start the bot", private_only=True)
async def start_func(bot: Nigger, msg):
    try:
        if not module.START:
            Nigger.log(LOADED_BUT_EMPTY.format("start", "start"), "warn")
            return
        text = await replace(module.START, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS))
        else:
            await msg.react(text)
    except AttributeError:
        pass


@Nigger.cmd('start', description="Start the bot", group_only=True)
async def start_in_groups_func(bot: Nigger, msg):
    try:
        if not module.START_IN_GROUPS:
            return  # No warning
        text = await replace(module.START_IN_GROUPS, msg, bot)
        await msg.react(text)
    except AttributeError:
        pass
