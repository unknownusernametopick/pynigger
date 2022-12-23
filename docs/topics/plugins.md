# Creating Plugins

Some Python knowledge is required to create plugins in general. Therefore, I highly recommend you to learn Python first. [Please see this FAQ](/meta/faqs#learn-python)

!!! note

    - All plugins must be added to the **plugins** folder.
    - Plugins must end with .py extension


Here's a sample code for a new plugin

```python
# Import class 'Ger' in every plugin
from pyger import Ger, Message

# use 'Ger.cmd' decorator to create commands
# @Ger.cmd('name', description="...", owner_only=False, extra_filters=None, group=0, private=False) - defaults

@Ger.cmd('sample', "Sample command for bot")  # or @Ger.command('sample', description="Sample command for bot")
async def sample_function(bot: Ger, msg: Message):
    # 'msg.react()' is 'msg.reply()' with del_in added argument
    await msg.react('This will be the reply when /sample is sent.')
```

But anyway, you can create easier plugins like text plugins with no python knowledge whatsoever.

```python
from pyger import Ger


@Ger.cmd('command_name', description='command description')
async def text_plugin(bot, msg):
    text = 'your text here'
    await msg.react(text)
```

For example, below plugin has a command ``/greet`` and the bot will reply with `Welcome to the Bot`

```python
from pyger import Ger


@Ger.cmd('greet', "Greet the user")
async def text_plugin(bot, msg):
    text = 'Welcome to the Bot'
    await msg.react(text)
```
