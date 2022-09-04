from sqlalchemy import Column, TEXT, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(TEXT)
    consent = Column(Integer)