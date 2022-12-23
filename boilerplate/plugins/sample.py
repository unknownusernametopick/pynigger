# Import class 'Ger' in every plugin
from pyger import Ger, Message


# use 'Ger.cmd' decorator to create commands
# @Ger.cmd(cmd=None, description=None, owner_only=False, extra_filters=None, group=0, private=False) - defaults

@Ger.cmd('sample', "Sample command for bot")  # or @Ger.command('sample', description="...")
async def sample_function(bot: Ger, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
