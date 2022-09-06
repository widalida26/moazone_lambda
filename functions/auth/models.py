from sqlalchemy import Column, TEXT, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'
    user_id = Column(TEXT, nullable=False, primary_key=True)
    credit = Column(Float, nullable=False)
    consent = Column(Integer)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(TEXT)
    consent = Column(Integer, nullable=True)