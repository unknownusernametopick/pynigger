from pyger import Ger, filters
from pyger.config import settings, ENV
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Ger.cmd(private_only=True, extra_filters=~filters.edited & filters.incoming, group=-1)
async def must_join_channel(bot: Ger, msg: Message):
    if ENV.DATABASE_URL:
        from pyger.plugins.helpers import db
        if (await db.has_table("bans")) and msg.from_user.id in (await db.get_all_primary_keys("bans")):
            await msg.reply("You have been banned from using this bot !", quote=True)
            await msg.stop_propagation()
            return
    module = settings()
    try:
        chats = module.MUST_JOIN
    except AttributeError:
        chats = []
    if not chats:
        Ger.log("Addon must_join is loaded but no chat is listed in MUST_JOIN var of settings", "warn")
        return
    nope = []
    for chat in chats:
        try:
            await bot.get_chat_member(chat, msg.from_user.id)
        except UserNotParticipant:
            nope.append(chat)
        except ChatAdminRequired:
            Ger.log(f"I'm not admin in the {chat} Chat !", "warning")
    if not nope:
        return
    buttons = []
    for i in nope:
        c = await bot.get_chat(i)
        if isinstance(i, int):
            i = c.title
        buttons.append([InlineKeyboardButton(f"✨ Join {i} ✨", url=c.invite_link)])
    try:
        await msg.reply(
            f"You must join my {'chats' if len(nope)>1 else 'chat'} to use me. Click on below buttons to join {'them' if len(nope)>1 else 'it'} \n\nAfter joining try again !",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        await msg.stop_propagation()
    except ChatWriteForbidden:
        pass
