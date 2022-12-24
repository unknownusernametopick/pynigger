from pyrogram.methods import Methods
from .command import Command
from .inline import Inline
from .callback import Callback

# from .admins import Admins


class Mechanism(Methods, Command, Inline, Callback):
    pass
