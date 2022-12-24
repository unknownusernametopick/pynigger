from pynigger import Nigger

try:
    from tinydb import TinyDB, Query
except ImportError:
    import os

    Nigger.log("Installing tinydb...")
    os.system("pip3 install tinydb~=4.6.1")
    from tinydb import TinyDB, Query

db = TinyDB("db.json")
Nigger.log("Initialized TinyDB")
