
from typing import Union
from ..config import settings, ENV
from pyrogram import filters as f
from pyrogram.methods.decorators.on_message import OnMessage


command_data = {"total_commands": 0, "all_commands": {}, "sudo_commands": []}


class Command(OnMessage):
    @staticmethod
    def command(
        cmd: Union[str, list[str]] = None,
        description: str = None,
        group: int = 0,
        owner_only: bool = False,
        sudo_only: bool = False,
        private_only: bool = False,
        group_only: bool = False,
        channel_only: bool = False,
        extra_filters=None
    ):
        """This decorator is used to handle messages. Mainly used to create commands. All arguments are  optional.
        You can also use the alias ``Ger.cmd`` instead of ``Ger.command``.

        Parameters:

            cmd (str | list[str], optional): Command(s) that triggers your function. Defaults to None, which is helpful you only want to use extra_filters argument.

            description (str,  optional): Command description to create Bot Menu. Defaults to None. [Read More](/topics/bot-menu)

            group (int, optional): Define a group for this handler. Defaults to 0. [Read More](https://docs.pyrogram.org/topics/more-on-updates#handler-groups)

            owner_only (bool, optional): Allow only owner to use this command. Defaults to False.

            sudo_only (bool, optional): Allow only sudos to use this command. Includes owner as sudo automatically. Defaults to False.

            private_only (bool, optional): Only handle messages for private chats. Bot will ignore messages in groups and channels. Defaults to False.

            group_only (bool, optional): Only handle messages for groups. Bot will ignore messages in private chats and channels. Defaults to False.

            channel_only (bool, optional): Only handle messages for channels. Bot will ignore messages in private chats and groups. Defaults to False.

            extra_filters (pyrogram.filters, optional): Extra filters to apply in your function. Import ``filters`` from pyrogram or pyger to use this. See example below.

        Examples:

            ```python
            from pyger import Ger

            # The normal way. Bot will reply to command ``/greet`` sent anywhere and by anyone.
            @Ger.command('greet', description='Greet the user')

            # or
            @Ger.cmd('greet', 'Greet the user')

            # Bot will reply only to owner, that is, the user whose id is set as OWNER_ID in environment variables.
            # Others will be ignored.
            @Ger.command('greet', owner_only=True)

            # Bot will reply only to sudo users or owner, that is, users set as SUDO_USERS or OWNER_ID in environment variables.
            # Others will be ignored.
            @Ger.command('greet', sudo_only=True)

            # Bot will reply only if message is sent in private chat (aka pm).
            # Messages in groups and channels will be ignored.
            @Ger.command('greet', private_only=True)

            # Bot will reply only if message is sent in groups.
            # Messages in groups and private chats will be ignored.
            @Ger.command('greet', group_only=True)

            # Bot will reply only if message is sent in channels.
            # Messages in private chats and groups will be ignored.
            @Ger.command('greet', channel_only=True)


            # Filter all messages.

            # Use positive integer to execute after executing another function in default group that also filtered this message.
            @Ger.command(group=1)

            # or Use negative integer to execute before executing another function in default group that also filtered this message.
            @Ger.command(group=-1)

            # Don't use this as other functions won't work.
            @Ger.command()


            # Filter other type of messages using extra_filters.

            # Import filters from pyrogram or pyger.
            from pyger import filters

            # Filter only media messages.
            @Ger.command(extra_filters=filters.media)

            # Filter only text messages.
            @Ger.command(extra_filters=filters.text)

            # Filter only messages sent by 'GerProgrammer'.
            @Ger.command(extra_filters=filters.user('GerProgrammer'))

            # Filter only messages sent in 'GerBotsChat'
            @Ger.command(extra_filters=filters.chat('GerBotsChat'))

            # Filter only messages with the word 'baby'.
            @Ger.command(extra_filters=filters.regex('baby'))

            # Filter all media messages sent by bots.
            @Ger.command(extra_filters=filters.bot & filters.media)

            # Filter all messages sent by bots except media messages.
            @Ger.command(extra_filters=filters.bot & ~filters.media)

            # Filter either media messages or text messages.
            @Ger.command(extra_filters=filters.text | filters.media)
            ```
        """
        if isinstance(cmd, str):
            cmd = [cmd]
        if owner_only or sudo_only:
            command_data["sudo_commands"] += cmd
        prefixes = settings().CMD_PREFIXES
        if not cmd and not extra_filters:
            filters_ = f.all
        elif cmd and extra_filters:
            for c in cmd:
                if c not in command_data["all_commands"]:
                    command_data["total_commands"] += 1
                    command_data["all_commands"][c] = ""
            filters_ = f.command(cmd, prefixes=prefixes) & extra_filters
        elif extra_filters:
            filters_ = extra_filters
        else:
            for c in cmd:
                if c not in command_data["all_commands"]:
                    command_data["total_commands"] += 1
                    command_data["all_commands"][c] = ""
            filters_ = f.command(cmd, prefixes=prefixes)
        if cmd and description:
            for c in cmd:
                command_data["all_commands"][c] = description
        if sudo_only:
            filters_ = filters_ & f.user(ENV().SUDO_USERS+ENV().OWNER_ID)
        elif owner_only:
            filters_ = filters_ & f.user(ENV().OWNER_ID)
        if private_only:
            filters_ = filters_ & f.private
        if group_only:
            filters_ = filters_ & f.group
        if channel_only:
            filters_ = filters_ & f.channel
        decorator = OnMessage.on_message(filters_, group)
        return decorator

    cmd = command  # alias
