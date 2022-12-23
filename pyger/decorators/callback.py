
from ..config import ENV
from typing import Union
from ..logger import logger
from pyrogram import filters as f
from pyrogram.methods.decorators.on_callback_query import OnCallbackQuery


class Callback(OnCallbackQuery):
    @staticmethod
    def callback(
        query: Union[str, list[str]] = None,
        startswith: bool = False,
        owner_only: bool = False,
        sudo_only: bool = False,
        group: int = 0,
        filters=None
    ):
        """This decorator is used to handle callback queries. All arguments are optional.

        Parameters:

            query (str | list[str], optional): Query on which your function is called. Defaults to None, to handle all queries if your function handles all or if using 'filters'

            startswith (bool, optional): Set to True if you want your function to handle all queries starting with the query_string. Defaults to False.

            owner_only (bool, optional): Allow only owner to use this command. Defaults to False.

            sudo_only (bool, optional): Allow only sudos to use this command. Includes owner as sudo automatically. Defaults to False.

            group (int, optional): Define a group for this handler. Defaults to 0. [Read More](https://docs.pyrogram.org/topics/more-on-updates#handler-groups)

            filters (pyrogram.filters, optional): Extra filters to apply in your function. Import ``filters`` from pyrogram or pyger to use this. See example below.

        Examples:

            ```python
            from pyger import Ger

            # The normal and easiest way.
            # Bot will execute function, if button with callback_data 'first_button' is pressed/clicked.
            @Ger.callback('first_button')

            # Handle multiple callback queries in one function. Mainly used to show same result or do some other pythonic thing, like if-else loop.
            # Bot will execute same function, if 'first_button' or 'second_button' is pressed/clicked.
            @Ger.callback(['first_button', 'second_button'])

            # Function will only be triggered if owner presses the button, that is, the user whose id is set as OWNER_ID in environment variables.
            # Others will be ignored.
            @Ger.callback('first_button', owner_only=True)

            # Function will only be triggered if sudo users or owner presses the button, that is, users set as SUDO_USERS or OWNER_ID in environment variables.
            # Others will be ignored.
            @Ger.callback('first_button', sudo_only=True)

            # Filter/Handle all queries.

            # Use positive integer to execute after executing another function in default group that also filtered this query.
            @Ger.callback(group=1)

            # or Use negative integer to execute before executing another function in default group that also filtered this query.
            @Ger.callback(group=-1)

            # Don't use this as other functions that handle queries won't work.
            @Ger.callback()

            # Filter other type of queries using 'filters' argument.

            # Import filters from pyrogram or pyger.
            from pyger import filters

            # Filter only queries by 'GerProgrammer' and 'Designatory'.
            @Ger.callback(filters=filters.user(['GerProgrammer', 'Designatory']))

            # Filter only queries done in 'NiGGeR_BotsChat'
            @Ger.callback(filters=filters.chat('NiGGeR_BotsChat'))

            # Filter only queries ending with the word 'baby'.
            @Ger.callback(filters=filters.regex(r'baby$'))

            # Filter all queries with the word 'hello' AND which are done in 'NiGGeR_BotsChat'.
            @Ger.callback(filters=filters.chat('NiGGeR_BotsChat') & filters.regex('hello'))
            # or
            @Ger.callback('hello', filters=filters.chat('NiGGeR_BotsChat'))

            # Filter all queries with the word 'bots' OR which are done in 'NiGGeR_BotsChat'
            @Ger.callback(filters=filters.chat('NiGGeR_BotsChat') | filters.regex('hello'))

            # Filter all queries with the word 'bots' BUT which are NOT done in 'NiGGeR_BotsChat'
            @Ger.callback(filters=~filters.chat('NiGGeR_BotsChat') & filters.regex('hello'))
            # or
            @Ger.callback(filters=filters.regex('hello') & ~filters.chat('NiGGeR_BotsChat'))
            ```
        """
        # ToDo:
        #   case_sensitive argument
        if isinstance(query, list):
            cmd_filter = f.create(lambda _, __, query_: query_.data.lower() in query)
        elif isinstance(query, str):
            query = query.lower()
            if not startswith:
                cmd_filter = f.create(lambda _, __, query_: query_.data.lower() == query)
            else:
                cmd_filter = f.create(lambda _, __, query_: query_.data.lower().startswith(query))
        elif not query:
            cmd_filter = None
        else:
            logger.warn(f'Callback: query cannot be of type {type(query)} - {query}]')
            return
        if filters:
            filters_ = cmd_filter & filters
        else:
            filters_ = cmd_filter
        if sudo_only:
            filters_ = filters_ & f.user(ENV().SUDO_USERS+ENV().OWNER_ID)
        elif owner_only:
            filters_ = filters_ & f.user(ENV().OWNER_ID)
        decorator = OnCallbackQuery.on_callback_query(filters_, group)
        return decorator

    cb = callback  # alias
