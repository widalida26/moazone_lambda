import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = os.environ.get('DATABASE_USERNAME')
db_password = os.environ.get('DATABASE_PASSWORD')
db_host = os.environ.get('DATABASE_HOST')
db_port = os.environ.get('DATABASE_PORT')
db_name = os.environ.get('DATABASE_NAME')

db_url =  f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8"

class connect_engine:
    def __init__(self):
        self.engine = create_engine(db_url, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind = self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn