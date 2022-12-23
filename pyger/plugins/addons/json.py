import os
from pyger import Ger, Message


@Ger.cmd("json", owner_only=True)
async def json(_, msg: Message):
    if not msg.reply_to_message:
        await msg.reply("Please reply to a message", quote=True)
        return
    data = str(msg.reply_to_message)
    if len(data) > 4096:
        with open("message.json", "w", encoding="utf-8") as f:
            f.write(data)
        await msg.reply_document("message.json", quote=True)
        os.remove("message.json")
    else:
        await msg.react(data)


@Ger.cmd("jsondoc", owner_only=True)
async def jsondoc(_, msg: Message):
    if not msg.reply_to_message:
        await msg.reply("Please reply to a message", quote=True)
        return
    data = str(msg.reply_to_message)
    with open("message.json", "w", encoding="utf-8") as f:
        f.write(data)
    await msg.reply_document("message.json", quote=True)
    os.remove("message.json")
