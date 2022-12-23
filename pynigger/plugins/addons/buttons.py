from pynigger import Nigger
from pynigger.plugins.ger import HOME_BUTTON, MAIN_BUTTONS
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from pynigger.plugins.helpers import replace, module, replace_commands


@Nigger.callback(query=['home', 'about', 'help'])
async def basic_cb(bot: Nigger, cb: CallbackQuery):
    # No Warns Cuz Personalized
    chat_id = cb.from_user.id
    message_id = cb.message.message_id
    if cb.data == 'home':
        text = await replace(module.START, cb.message, bot)
        buttons = MAIN_BUTTONS
    elif cb.data == 'about':
        text = await replace(module.ABOUT, cb.message, bot)
        buttons = HOME_BUTTON
    else:
        text = str(module.HELP)
        if "{commands}" in text:
            text = await replace_commands(bot, text)
        text = await replace(text, cb.message, bot)
        buttons = HOME_BUTTON
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )
