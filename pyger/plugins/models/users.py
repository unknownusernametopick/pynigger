
from pyger.database.sql import Base
from sqlalchemy import Column, BigInteger, String


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    lang = Column(String)

    def __init__(self, user_id: int, lang: str = "en"):
        self.user_id = user_id
        self.lang = lang
