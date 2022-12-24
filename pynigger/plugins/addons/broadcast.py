from pynigger import Nigger, Message
from pynigger.plugins.helpers import db


@Nigger.cmd("broadcast", owner_only=True)
async def broadcast(bot: Nigger, msg: Message):
    if not msg.reply_to_message and len(msg.command) == 1:
        await msg.reply("Please reply to a message or pass some text",
                        quote=True)
        return
    text = (msg.reply_to_message.text
            if msg.reply_to_message else msg.text[len("/broadcast "):])
    users = await db.get_all_primary_keys("users")
    await msg.reply_text("Starting Broadcast...")
    count = 0
    for user in users:
        try:
            await bot.send_message(user, text)
            count += 1
        except Exception as e:
            Nigger.log(
                f"Exception occurred while sending message to user with id {user}: {e}",
                "warning",
            )
    await msg.react(
        f"Broadcast done successfully to {count} users out of {len(users)}")
