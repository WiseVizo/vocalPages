from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE = 'mysql+pymysql://root:root@localhost:3306/fastapidb'
URL_DATABASE = 'mysql+pymysql://rootuser:test1234!@fastapi-aws-database.cfmamgu4ss9g.ap-south-1.rds.amazonaws.com:3306/fastapidb'
engine = create_engine(URL_DATABASE)
sesion_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()  