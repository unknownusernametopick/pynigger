# ChangeLog

Latest Version: `v1.1.2`

---

<a name="v1.1.2"></a>
### v1.1.2 <small>- April 10, 2022</small>

- Added function [to_webp][pyger.helpers.stickers.to_webp] (`pyger.helpers.stickers.to_webp`) to package [helpers](/helpers)

---

<a name="v1.1.0"></a>
### v1.1.0 <small>- April 10, 2022</small>

- **Additions**:
    - Added dark mode to documentation.
    - Added [START_IN_GROUPS](/topics/settings#start_in_groups) option to set message that will be replied when `/start` command is sent in groups.
    - Added [LOG_CHAT](/start/variables#non-environment-variables) environment variable to set a log chat id for logging error to Telegram.
    - Added [`Ger.log_tg`][pyger.client.Ger.log_tg] method to log messages to Telegram [`LOG_CHAT`](/start/variables#non-environment-variables)
    - Added `Ger.admins` decorator to allow only admins to use a particular command. [Read More](/decorators/admins)
    - Added [`pyger.helpers`](/helpers) package for some helpful functions.
    - Added localization option to have multi-language support for your bot.
    - Added helpers for sync and async command execution using subprocess in `pyger.helpers.system`
    - Added properties to [class Ger](/classes/ger):
        - [total_plugins][pyger.client.Ger.total_plugins]
        - [all_plugins][pyger.client.Ger.all_plugins]
        - [total_commands][pyger.client.Ger.total_commands]
        - [all_commands][pyger.client.Ger.all_commands]
        - [sudo_commands][pyger.client.Ger.sudo_commands]
    - Added properties to [class Message](/classes/message):
        - [args][pyger.methods.message.Message.args]
        - [input][pyger.methods.message.Message.input]
        - [ref][pyger.methods.message.Message.ref]
    - Added methods to [class Message](/classes/message):
        - [get_ref_user][pyger.methods.message.Message.get_ref_user]
    - Added a special keyword [`{commands}`](/topics/customization#special-keywords) which will be automatically replaced with commands in [HELP](/topics/settings#help-option) message.
    - Added announcement bar in documentation.
    - Added documentation for class `Message`, decorator `Admins` and also for all added things.
- **Improvements**:
    - Improved methods in `pyger.database.sql.Database`.
    - Improved Documentation structure.
    - Documented and Improved `react` method of `Message` class.
    - Nested plugins (plugins in subdirectories) are now also loaded.
    - Auto add commands to help message if default set up is used or `{commands}` is in help message.
    - `Ger.data()` is now `Ger().data`, i.e, a property instead of a staticmethod. It will no longer take any arguments.
    - `Ger.sudo_commands()` is now `Ger().sudo_commands`, i.e, a property instead of a staticmethod.
    - `Ger().langs` lists all languages if localization is set up. It is a property so doesn't need to be called with round brackets ().
    - Better Plugins Loading.
    - `pyger.database.sql.Database.tables_dict` is now a public method.
    - Renamed commands `ban`, `unban` and `banlist` to `botban`, `botunban` and `botbanlist` respectively to prevent clashes with general group commands.
    - Removed pyromod as a dependency (temporarily till its features are added.)
- **Bugfixes**:
    - Fixed local deploys for Windows.
    - Fix same command listed multiple times in `Ger.data['all_commands']`
    - Fix sudo commands list, [Ger().sudo_commands][pyger.client.Ger.sudo_commands].
    - `Message.react` now returns the message just like it should
    - Fixed non-existent users' return value in `pyger.database.sql.Database.get`
    - Handle `None` value for [settings.PLUGINS](/topics/settings#plugins)
    - Fixed `pyger.database.sql.Database.tables_dict` method.

---

<a name="v1.0.2"></a>
### v1.0.2 <small>- April 7, 2022</small>

- Specify minimum python version which is `3.9`, in docs and pypi.
- More user-friendly boilerplate.

---

<a name="v1.0.1"></a>
### v1.0.1 <small>- April 7, 2022</small>

- Fix broken CLI due to bad imports.
- Add `dev-requirement.txt` for docs and pypi

---

<a name="v1.0.0"></a>
### v1.0.0 <small>- April 6, 2022</small>

- Enhanced project settings, inspired from django.
- Added brand new addons for additional features in bots.
- Brand-new documentation using Mkdocs instead of Sphinx.
- Database migration methods for `pyger.database.sql.Database` class like `add_column`, `remove_column`, etc.
- Added other useful methods like 
- Improved boilerplate in favour of new features.
- Added documentation for [project settings](/topics/settings) using `settings.py`
- Removed customization options from `Ger.activate()` as they can be configured using `settings.py` now.
- Removed `pyger.database.postgres` in favour of `pyger.database.sql`.
- Added sudo users support for bots which can be set using `SUDO_USERS` environment variable.
- Allow username as `OWNER_ID` instead of only `user_id`
- Pre-made models for `users` and `bans` table.
- And much, much more! 

---


<a name="v0.4.0"></a>
### v0.4.0 <small>- March 15, 2022</small>

- BugFixes and improvements in SQL helper functions.
- Make Database related dependencies optional and automated.
- Class Database instead of functions
- Rollback at exceptions
- Raw SQL for getting all rows as it usually depends on python class instead of data in table
- Raise TableNotFound if it doesn't exist instead of returning None
- Rename `pyger.databases.postgres` to `pyger.databased.sql` in favour of other sql databases.
- Allow other type of Database URls
- Add attributes like `session`, `base`, `engine` to Database.


<a name="v0.3.0"></a>
### v0.3.0 <small>- January 28, 2022</small>

- Additions
    - Use inline mode and callback buttons more easily.
    - Handle inline queries using `Ger.inline()`.
    - Handle callback queries using `Ger.callback()`.
    - Load plugins from multiple directories. Instead of passing a 'str' to 'activate()' function, pass a list.
    - Allow passing other keyword arguments while creating bot client.
    - Override the in-built/default plugins automatically as they are loaded later now.
- Pyger CLI
    - Added optional argument ['-v', '--version'] to see currently installed version.
    - Removed optional argument ['-h', '--help'] as passing no argument does the same thing.
    - Made unnecessary arguments private.
- Improvements
    - Improved PyPI Home page and Project Readme.
    - Improved Boilerplate.
    - Upgraded TelegramDB.
    - Separated constants.
    - Renamed default plugins file to remove confusion.
- BugFixes
    - Fixed `ModuleNotFoundError` for psycopg2 (missing requirement).
- Documentation
    - Added documentation for [all decorators](/decorators). [Ger.callback][pyger.decorators.callback.Callback.callback] and [Ger.inline][pyger.decorators.inline.Inline.inline]
    - Added a temporary logo. Thanks to [Designatory](https://t.me/designatory).
    - Removed dark mode.
    - Separated older releases. [Can be found here](/meta/older-releases).
    - Enable Single Version option.
    - Changed the color for annoying visited links.
    - Changed templates for footer and header.
    - Add homepage to toctree.
    - Custom 404 page. Thanks to [Designatory](https://t.me/designatory).
    - Other Improvements.
