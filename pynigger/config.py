
import os
from typing import Union
from .logger import logger
from dotenv import load_dotenv
from pynigger import settings as s
from importlib import import_module
from pynigger.plugins import nigger as h


load_dotenv('.env')

default = None


def settings():
    global default
    if default:
        return default
    if os.path.exists('settings.py'):
        mod = import_module('settings')
    elif os.path.exists('data.py'):
        logger.warn("File name 'data.py' for settings is deprecated. Please rename it to 'settings.py' instead.")
        mod = import_module('data')
    else:
        logger.warn("Settings file not found. Default values will be used.")
        mod = import_module('pynigger.settings')
    for i in dir(s):
        if not i.isupper():
            continue
        if "NIGGER_BOTS" in mod.__dict__ and getattr(mod, "NIGGER_BOTS") and i == "ADDONS":
            continue
        try:
            getattr(mod, i)
        except AttributeError:
            setattr(mod, i, getattr(s, i))
    for i in ["NIGGER_BOTS", "FULL_MESSAGES", "CUSTOM_USERS_TABLE", "NO_BUTTONS", "REMOVE_ADDONS"]:  # my personalization (not in settings.py)
        try:
            getattr(mod, i)
        except AttributeError:
            setattr(mod, i, False)
    prefixes = getattr(mod, "CMD_PREFIXES")
    if not isinstance(prefixes, list):
        setattr(mod, "CMD_PREFIXES", [prefixes])
    if getattr(mod, "NIGGER_BOTS") or os.getenv("NIGGER_BOTS", ""):
        # FULL_MESSAGES
        if "FULL_MESSAGES" not in mod.__dict__ or not getattr(mod, "FULL_MESSAGES"):
            # START
            setattr(mod, "START", h.START.replace("{1}", getattr(mod, "START")))
            # HELP
            setattr(mod, "HELP", h.HELP.replace("{1}", getattr(mod, "HELP")))
            # REPO
            try:
                rep = getattr(mod, "REPO")
            except AttributeError:
                rep = ""
            # ABOUT
            setattr(
                mod,
                "ABOUT",
                h.ABOUT
                .replace("{1}", getattr(mod, "ABOUT"))
                .replace("{2}", (("\n\nSource Code : [Click Here](https://github.com/unknownusernametopick/"+rep+")") if rep else ""))
            )
        # MUST_JOIN
        if not getattr(mod, "MUST_JOIN") and ("special" in os.getenv("MUST_JOIN", "") or os.getenv("NIGGER_BOTS", "")):
            setattr(mod, "MUST_JOIN", ["NiGGeR_Bots", "NiGGeR_BotsChat"])

        # ADDONS
        if "ADDONS" not in mod.__dict__:
            from pynigger.plugins import addons
            plugs = [f for f in os.listdir(addons.__path__[0]) if f.endswith(".py")]
            if getattr(mod, "NO_BUTTONS"):
                plugs.remove("buttons.py")
            rem = getattr(mod, "REMOVE_ADDONS")
            if rem:  # Bad code?
                for p in rem:
                    if p in plugs:
                        plugs.remove(p)
                    elif p+".py" in plugs:
                        plugs.remove(p+".py")
            setattr(mod, "ADDONS", plugs)

        # DATABASE_TABLES
        tables = getattr(mod, "DATABASE_TABLES")
        if "bans" not in tables:
            tables.append("bans")

        # CUSTOM_USERS_TABLE
        if ("CUSTOM_USERS_TABLE" not in mod.__dict__ or not getattr(mod, "CUSTOM_USERS_TABLE")) and "users" not in tables:
            tables.append("users")
        setattr(mod, "DATABASE_TABLES", tables)

        # CMD_PREFIXES
        setattr(mod, "CMD_PREFIXES", ["/", "!"])

    # Set Timezone to env so there's no circular import for logger.py
    os.environ["TIMEZONE"] = getattr(mod, 'TIMEZONE')
    default = mod  # Cache
    return mod


class ENV:
    API_ID = os.environ.get("API_ID", "").strip()
    API_HASH = os.environ.get("API_HASH", "").strip()
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
    OWNER_ID = os.environ.get("OWNER_ID", "").strip().split(" ")
    LOG_CHAT = os.environ.get("LOG_CHAT", "").strip()
    SUDO_USERS = os.environ.get("SUDO_USERS", "").strip().split(" ")
    DB_SESSION = os.environ.get("DB_SESSION", "").strip()
    DB_CHAT_ID = os.environ.get("DB_CHAT_ID", "").strip()
    DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()
    if DATABASE_URL:
        if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
            DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

    def __init__(self):
        module = settings()

        if not self.API_ID:
            logger.critical("No API_ID found. Exiting...")
            raise SystemExit
        if not self.API_HASH:
            logger.critical("No API_HASH found. Exiting...")
            raise SystemExit
        if not self.BOT_TOKEN:
            logger.critical("No BOT_TOKEN found. Exiting...")
            raise SystemExit
        if not self.LOG_CHAT:
            self.LOG_CHAT = 0

        if "special" in self.OWNER_ID or getattr(module, "NIGGER_BOTS"):
            if not self.OWNER_ID or not self.OWNER_ID[0]:
                self.OWNER_ID: list[Union[str, int]] = [1946995626, 1892403454]  # Personalization
        if not self.OWNER_ID or not self.OWNER_ID[0]:
            self.OWNER_ID = [0]
            # logger.warn("No OWNER_ID found. Please set one. Exiting...")
            # raise SystemExit

        try:
            self.API_ID = int(self.API_ID)
        except ValueError:
            logger.critical("API_ID is not a valid integer. Exiting...")
            raise SystemExit
        if self.DB_CHAT_ID:
            try:
                self.DB_CHAT_ID = int(self.DB_CHAT_ID)
            except ValueError:
                logger.critical("DB_CHAT_ID is not a valid integer. Exiting...")
                raise SystemExit
        owners = []
        for o in self.OWNER_ID:
            if isinstance(o, str) and o.isdigit():
                owners.append(int(o))
            else:
                owners.append(o)
        self.OWNER_ID = owners

        sudos = []
        for o in self.SUDO_USERS:
            if o.isdigit():
                sudos.append(int(o))
            else:
                sudos.append(o)
        self.SUDO_USERS = sudos

        if self.LOG_CHAT and ("special" in self.LOG_CHAT or os.getenv("NIGGER_BOTS", "")) and getattr(module, "NIGGER_BOTS"):
            self.LOG_CHAT = -1001682015859  # Nigger Bots Logs
        try:
            self.LOG_CHAT = int(self.LOG_CHAT)
        except ValueError:
            logger.critical("LOG_CHAT is not a valid integer. Exiting...")
            raise SystemExit
