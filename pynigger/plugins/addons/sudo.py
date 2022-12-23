from pynigger import Nigger, Message


@Nigger.cmd("sudo", owner_only=True)
async def sudo(bot: Nigger, msg: Message):
    text = "Sudo Commands Available: \n"
    num = 0
    for i in bot.sudo_commands:
        num += 1
        text += f"\n{num}) /{i}"
    await msg.react(text)
