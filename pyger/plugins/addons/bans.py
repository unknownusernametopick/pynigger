from pyger import Ger
from pyger.config import ENV
from pyger.plugins.helpers import db
from pyrogram.errors import PeerIdInvalid


@Ger.cmd("botban", owner_only=True)
async def ban_users(bot: Ger, msg):
    if len(msg.command) == 1:
        user_id = None
        if msg.reply_to_message:
            for word in msg.reply_to_message.text.split():
                if word.isdigit() and len(word) == 10:
                    user_id = int(word)
        else:
            await msg.reply("Pass an ID", quote=True)
            return
        if user_id:
            reason = await bot.get_messages(msg.chat.id, msg.reply_to_message.message_id)
            try:
                reason = reason.reply_to_message.link
            except AttributeError:
                reason = None
            await db.set("bans", user_id, {"reason": reason})
            await msg.reply(f"Banned `{user_id}`")
    else:
        user_id = msg.command[1]
        if user_id.isdigit() and len(user_id) == 10:
            user_id = int(user_id)
        else:
            await msg.reply("Wrong ID", quote=True)
            return
        if user_id:
            if user_id in ENV().OWNER_ID:
                await msg.reply(f"Banned `{user_id}`", quote=True)
                await msg.reply(f"Seriously banned.", quote=True)
                await msg.reply(f"I'm not kidding.", quote=True)
                return
            await db.set("bans", user_id, {"reason": None})
            await msg.reply(f"Banned `{user_id}`", quote=True)


@Ger.cmd("botunban", owner_only=True)
async def unban_users(_, msg):
    if len(msg.command) == 1:
        await msg.reply("Please pass a user id or username", quote=True)
    else:
        user_id = msg.command[1]
        if user_id.isdigit() and len(user_id) == 10:
            user_id = int(user_id)
        else:
            await msg.reply("Wrong ID", quote=True)
            return
        if user_id:
            if user_id in await db.get_all_data("bans"):
                await db.delete("bans", user_id)
                await msg.reply(f"Unbanned `{user_id}`", quote=True)
            else:
                await msg.reply("Wasn't banned...", quote=True)


@Ger.cmd("botbanlist", owner_only=True)
async def ban_list(bot: Ger, msg):
    number = 0
    banned = await db.get_all_data("bans")
    if len(banned) == 0:
        text = "No one is banned currently"
    else:
        text = f'**Banned Users [{len(banned)}]**'
        try:
            users = await bot.get_users([i["user_id"] for i in banned])
            for user in users:
                number = number+1
                user_text = f"\n\n{number}) {user.mention} [`{user.id}`]"
                reason = [i["reason"] for i in banned if i["user_id"] == user.id]
                if reason[0]:
                    user_text += f" - Reason - {reason[0]}"
                text += user_text
        except PeerIdInvalid:
            for i in banned:
                number = number+1
                try:
                    user = await bot.get_users(i["user_id"])
                    user_text = f"\n\n{number}) {user.mention} [`{user.id}`]"
                except PeerIdInvalid:
                    user_text = f"\n\n{number}) {i['user_id']}"
                if i["reason"]:
                    user_text += f" - Reason - {i['reason']}"
                text += user_text
    await msg.reply(text, quote=True)
