# Quick Start

Following these steps will allow you to see **Pyger** in action as quickly as possible.

!!! important
    Installation of Python with version 3.9 or above is required!

---

## Steps

1\. [Open up your terminal](/meta/faqs#terminal).

2\. Install Pyger with pip

```shell
$ pip3 install pyger
```

3\. Generate a boilerplate using Pyger's command-line tool.

```shell
$ pyger --boilerplate
```

4\. Enter the newly created `boilerplate` directory.

```shell
$ cd boilerplate
```

5\. [Open the file manager in current directory](/meta/faqs#file-manager).

6\. Edit the ``.env`` file and fill your `API_ID`, `API_HASH` and `BOT_TOKEN`. Get the API keys from [my.telegram.org](https://my.telegram.org) and bot token from [BotFather](https://telegram.me/BotFather).

7\. Run the bot using python

```shell
$ python3 bot.py
```

---

## What does this do?

The above steps will help you set up your bot and run it. You can use the command **/start** to check if your bot is actually running.

Your bot now has four default commands:

- `/start` - Start the bot (also works in groups)
- `/help` - See a help message for the bot.
- `/about` - About the bot.
- `/id` - Get Telegram ID (also works in groups)


Stop the bot using `Ctrl+C`.
