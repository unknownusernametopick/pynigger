from pyger import Ger


@Ger.cmd('id', description="Get your Telegram ID")
async def id_func(_, msg):
    if msg.chat.type == 'private':
        await msg.react("Your ID is `{}`".format(msg.from_user.id))
    else:
        if msg.reply_to_message:
            await msg.react("{}'s ID is `{}`".format(msg.reply_to_message.from_user.first_name, msg.reply_to_message.from_user.id))
        else:
            await msg.react("Chat ID is `{}` \n\nYour ID is `{}`".format(msg.chat.id, msg.from_user.id))
