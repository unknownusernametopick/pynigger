from pyger import Ger, Message


@Ger.cmd("sudo", owner_only=True)
async def sudo(bot: Ger, msg: Message):
    text = "Sudo Commands Available: \n"
    num = 0
    for i in bot.sudo_commands:
        num += 1
        text += f"\n{num}) /{i}"
    await msg.react(text)
