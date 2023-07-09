from sqlalchemy import Column, Integer, String
from db.session import Base


class Pill(Base):
    __tablename__ = "pill"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pill_name = Column(String)
    day = Column(String)
    time = Column(String)
