# Import class 'Nigger' in every plugin
from pynigger import Nigger, Message


# use 'Nigger.cmd' decorator to create commands
# @Nigger.cmd(cmd=None, description=None, owner_only=False, extra_filters=None, group=0, private=False) - defaults

@Nigger.cmd('sample', "Sample command for bot")  # or @Nigger.command('sample', description="...")
async def sample_function(bot: Nigger, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
