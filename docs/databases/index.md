# Using Databases

You can use any database you wish with Pyger, but we have provided a simple default setup for some databases, such as PostgreSQL and TelegramDB, to make them even easier to use.
By following this guide, you will have a basic understanding of how to use them.

---

## PostgreSQL (using sqlalchemy)

- **Database URL** - You need to add ``DATABASE_URL`` to ``.env``. If you are using Heroku boilerplate, leave it to **Heroku** and **pyger**. Otherwise, you can get a Database URL from [ElephantSQL](http://www.elephantsql.com)

- **Creating Tables** - You need to create all the tables with all columns you need. In Python, using Classes.

Below is a code example for a table named ``users`` with 3 columns named ``user_id``, ``name``, and ``aim``:

```python
# Import class 'Database' from pyger
from pyger.database.sql import Database
# Import basic sqlalchemy classes
from sqlalchemy import Column, Integer, String


# create a database instance
db = Database()


# Every class should inherit from 'db.base'
class Users(db.base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(Integer, primary_key=True)  # sql primary key (pk)
    name = Column(String)
    aim = Column(String)

    def __init__(self, user_id, name, aim=None):
        self.user_id = user_id
        self.name = name
        self.aim = aim


# Create Table
Users.__table__.create(checkfirst=True)
```

- **Querying Tables** - You can query tables using ``Session`` object or the in-built pyger functions.

    - [Using Session object](/databases/postgres#session-object)
    - [Using in-built functions](/databases/postgres#default-functions)

---

## Using Telegram as a Database

You can use Telegram as a Database, thanks to [this project](https://pypi.org/project/TelegramDB/).

**But How?** - [Read Documentation Here](/databases/telegram-as-database)

---

## TinyDB

TinyDB is a simple database which does not require a Database URL and is very simple. If you are a beginner, it is for you. [Read How to Use It](/databases/tinydb).

---
