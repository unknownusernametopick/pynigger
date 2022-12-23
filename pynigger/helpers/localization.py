
import os
import yaml
import json
from pynigger.logger import logger
from pynigger.config import settings


file = ""
folder = ""


def l10n_setup():
    global file
    global folder
    mod = settings()
    folder = getattr(mod, "LOCALIZATION")
    if folder:
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            logger.critical("Your localization path does not exist. Please correct it or set it to ''. Exiting...")
            raise SystemExit
        sup = ["english.yaml", "english.yml", "en.yaml", "en.yml", "english.json", "en.json"]
        for s in sup:
            if s in files:
                file = f"{folder}/{s}"
                break
        if not file:
            f = [f for f in files if f.endswith('.yaml') or f.endswith(".yml") or f.endswith('.json')]
            if f:
                file = f"{folder}/{f[0]}"
            else:
                logger.warn("Your localization directory does not have a json or yaml file")
        return True
    else:
        return False


async def l10n(lang: str = None):
    if not file:
        return
    if not lang:
        current_file = file
    else:
        current_file = ""
        for fi in os.listdir(folder):
            if lang in fi:
                current_file = fi
                break
        if not current_file:
            logger.warn(f"Lang '{lang}' not found. Choosing default.")
            current_file = file
    if current_file.endswith(".json"):
        return await json_load(current_file)
    elif current_file.endswith(".yaml") or current_file.endswith(".yml"):
        return await yaml_load(current_file)


async def yaml_load(path):
    with open(path, "r", encoding="utf-8") as fi:
        return yaml.safe_load(fi)


async def json_load(path):
    with open(path, "r", encoding="utf-8") as fi:
        return json.load(fi)


async def get_all_langs():
    if not file:
        return
    langs = {}
    for fi in os.listdir(folder):
        if fi.endswith(".yaml") or fi.endswith(".yml"):
            data = await yaml_load(fi)
        elif file.endswith(".json"):
            data = await json_load(file)
        else:
            continue
        langs[data["language"]] = fi
    return langs
