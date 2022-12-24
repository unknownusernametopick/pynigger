import os
import sys
import argparse
from pynigger.constants import __description__, __version__


def main():
    parser = argparse.ArgumentParser(
        prog="pynigger",
        description=__description__,
        usage="%(prog)s [options]",
        epilog="Enjoy the program :)",
        allow_abbrev=False,
        add_help=False,
    )
    cwd = os.getcwd()
    parser.add_argument(
        "-v",
        "--version",
        help="check the current pynigger version installed",
        action="store_true",
    )
    parser.add_argument(
        "-bp",
        "--boilerplate",
        help="create boilerplate in current folder",
        action="store_true",
    )
    parser.add_argument(
        "-bph",
        "--boilerplate-heroku",
        help="create boilerplate in current folder with added heroku support",
        action="store_true",
    )
    parser.add_argument("-s",
                        "--special",
                        help=argparse.SUPPRESS,
                        action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if args.version:
        print(f"v{__version__}")
        return
    if args.boilerplate_heroku or args.boilerplate or args.special:
        if args.special:
            print("Generating Boilerplate (for Nigger Bots)...")
            boilerplate(special=True)
        elif args.boilerplate_heroku:
            print("Generating Boilerplate (with Heroku Support)...")
            boilerplate()
        else:
            print("Generating Boilerplate...")
            boilerplate()
            files = ["app.json", "Procfile", "README.md", "requirements.txt"]
            for file in files:
                os.remove(cwd + "/boilerplate/" + file)
        print("Done. Boilerplate is ready!")


def boilerplate(special=False):
    os.system("pip install github-clone --quiet")
    if special:
        os.system(
            "ghclone https://github.com/unknownusernametopick/PyNigger/tree/master/boilerplate_nigger_bots"
        )
    else:
        os.system(
            "ghclone https://github.com/unknownusernametopick/PyNigger/tree/master/boilerplate"
        )
    os.system("pip uninstall github-clone --quiet -y")
