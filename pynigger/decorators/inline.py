from ..config import ENV
from ..logger import logger
from typing import Union, List
from pyrogram import filters as f
from pyrogram.methods.decorators.on_inline_query import OnInlineQuery


class Inline(OnInlineQuery):
    @staticmethod
    def inline(
        query: Union[str, List[str]] = None,
        startswith: bool = False,
        owner_only: bool = False,
        sudo_only: bool = False,
        group: int = 0,
        filters=None,
        # description: str = None,
        # allow_for_all: bool = False,
        # allow_devs: bool = False,
        # private_only: bool = False,
        # group_only: bool = False,
        # channel_only: bool = False,
        # disable_sudo: bool = False
    ):
        """This decorator is used to handle inline queries. All arguments are optional.

        Parameters:

            query (str | list[str], optional): Query on which your function is called. Pass a list to handle multiple queries. Defaults to None, to handle all queries if your function handles all or if you are using other 'filters'

            startswith (bool, optional): Set to True if you want your function to handle all queries starting with the 'query' string passed. Defaults to False.

            owner_only (bool, optional): Allow only owner to use this command. Defaults to False.

            sudo_only (bool, optional): Allow only sudos to use this command. Includes owner as sudo automatically. Defaults to False.

            group (int, optional): Define a group for this handler. Defaults to 0. [Read More](https://docs.pyrogram.org/topics/more-on-updates#handler-groups)

            filters (pyrogram.filters, optional): Extra filters to apply in your function. Import ``filters`` from pyrogram or pynigger to use this. See example below.

        Examples:

            ```python
            from pynigger import Nigger

            # The normal and easiest way.
            # Bot will show results / execute function, if 'hello' is searched by anyone.
            @Nigger.inline('hello')

            # Handle multiple inline queries in one function. Mainly used to execute same function or do some other pythonic thing, like if-else loop.
            # Bot will show results / execute function, if 'hello' or 'hey' is searched by anyone.
            @Nigger.inline(['hello', 'hey'])

            # Function will only be triggered if owner searches 'hello', that is, the user whose id is set as OWNER_ID in environment variables.
            # Others will be ignored.
            @Nigger.inline('hello', owner_only=True)

            # Function will only be triggered if sudo users or owner searches 'hello', that is, users set as SUDO_USERS or OWNER_ID in environment variables.
            # Others will be ignored.
            @Nigger.inline('hello', sudo_only=True)

            # Filter/Handle all queries.

            # Use positive integer to execute after executing another function in default group that also filtered this query.
            @Nigger.inline(group=1)

            # or Use negative integer to execute before executing another function in default group that also filtered this query.
            @Nigger.inline(group=-1)

            # Don't use this as other functions that handle queries won't work.
            @Nigger.inline()

            # Filter other type of queries using 'filters' argument.

            # Import filters from pyrogram or pynigger.
            from pynigger import filters

            # Filter only queries by 'GerProgrammer' and 'Designatory'.
            @Nigger.inline(filters=filters.user(['GerProgrammer', 'Designatory']))

            # Filter only queries done in 'NiGGeR_BotsChat'
            @Nigger.inline(filters=filters.chat('NiGGeR_BotsChat'))

            # Filter only queries ending with the word 'baby'.
            @Nigger.inline(filters=filters.regex(r'baby$'))

            # Filter all queries with the word 'hello' AND which are done in 'NiGGeR_BotsChat'.
            @Nigger.inline(filters=filters.chat('NiGGeR_BotsChat') & filters.regex('hello'))
            # or
            @Nigger.inline('hello', filters=filters.chat('NiGGeR_BotsChat'))

            # Filter all queries with the word 'bots' OR which are done in 'NiGGeR_BotsChat'
            @Nigger.inline(filters=filters.chat('NiGGeR_BotsChat') | filters.regex('hello'))

            # Filter all queries with the word 'bots' BUT which are NOT done in 'NiGGeR_BotsChat'
            @Nigger.inline(filters=~filters.chat('NiGGeR_BotsChat') & filters.regex('hello'))
            # or
            @Nigger.inline(filters=filters.regex('hello') & ~filters.chat('NiGGeR_BotsChat'))
            ```
        """
        # ToDo:
        #   case_sensitive argument
        if isinstance(query, list):
            cmd_filter = f.create(lambda _, __, query_: query_.query.lower() in query)
        elif isinstance(query, str):
            query = query.lower()
            if not startswith:
                cmd_filter = f.create(lambda _, __, query_: query_.query.lower() == query)
            else:
                cmd_filter = f.create(lambda _, __, query_: query_.query.lower().startswith(query))
        elif not query:
            cmd_filter = None
        else:
            logger.warn(f'Inline: query cannot be of type {type(query)} - {query}]')
            return
        if filters:
            filters_ = cmd_filter & filters
        else:
            filters_ = cmd_filter
        if sudo_only:
            filters_ = filters_ & f.user(ENV().SUDO_USERS+ENV().OWNER_ID)
        elif owner_only:
            filters_ = filters_ & f.user(ENV.OWNER_ID)
        decorator = OnInlineQuery.on_inline_query(filters_, group)
        return decorator

    il = inline  # alias
