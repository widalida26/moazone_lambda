from sqlalchemy import Column, TEXT, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(TEXT)
    consent = Column(Integer, nullable=True)

class SurveyInfo(Base):
    __tablename__ = 'new'
    index = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    gender = Column(TEXT)
    car = Column(TEXT)
    reality = Column(TEXT)
    child_num = Column(Integer)
    income_total = Column(Integer)
    income_type = Column(TEXT)
    edu_type = Column(TEXT)
    family_type = Column(TEXT)
    house_type = Column(TEXT)
    DAYS_BIRTH = Column(Integer)
    DAYS_EMPLOYED = Column(Integer)
    FLAG_MOBIL = Column(Integer)
    work_phone = Column(Integer)
    phone = Column(Integer)
    email = Column(Integer)
    occyp_type = Column(TEXT)
    family_size = Column(Integer)
    begin_month = Column(Integer)