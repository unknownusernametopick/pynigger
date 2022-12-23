from pyger import Ger
from pyger.plugins.ger import MAIN_BUTTONS
from pyrogram.types import InlineKeyboardMarkup
from pyger.plugins.helpers import replace, send_buttons, module, LOADED_BUT_EMPTY


@Ger.cmd('start', description="Start the bot", private_only=True)
async def start_func(bot: Ger, msg):
    try:
        if not module.START:
            Ger.log(LOADED_BUT_EMPTY.format("start", "start"), "warn")
            return
        text = await replace(module.START, msg, bot)
        if await send_buttons():
            await msg.react(text, reply_markup=InlineKeyboardMarkup(MAIN_BUTTONS))
        else:
            await msg.react(text)
    except AttributeError:
        pass


@Ger.cmd('start', description="Start the bot", group_only=True)
async def start_in_groups_func(bot: Ger, msg):
    try:
        if not module.START_IN_GROUPS:
            return  # No warning
        text = await replace(module.START_IN_GROUPS, msg, bot)
        await msg.react(text)
    except AttributeError:
        pass
