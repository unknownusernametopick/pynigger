from pyrogram.types import Message
from pyger import Ger, filters
from pyger.plugins.helpers import db


@Ger.cmd(extra_filters=~filters.edited & ~filters.service, group=2)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = await db.get("users", msg.from_user.id)
        if not q:
            await db.set("users", msg.from_user.id)


@Ger.cmd('stats', owner_only=True)
async def stats(_, msg: Message):
    users = await db.count("users")
    await msg.reply(f"Total Users : {users}", quote=True)
