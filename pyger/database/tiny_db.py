from pyger import Ger
try:
    from tinydb import TinyDB, Query
except ImportError:
    import os
    Ger.log('Installing tinydb...')
    os.system('pip3 install tinydb~=4.6.1')
    from tinydb import TinyDB, Query

db = TinyDB('db.json')
Ger.log('Initialized TinyDB')
