from sqlalchemy.engine import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore
# from sqlalchemy.ext.declarative import declarative_base #type: ignore

URL_DATABASE = 'mysql+pymysql://root:root@localhost:3306/mydb'
# URL_DATABASE = 'mysql+pymysql://rootuser:test1234!@fastapi-aws-database.cfmamgu4ss9g.ap-south-1.rds.amazonaws.com:3306/fastapidb'
engine = create_engine(URL_DATABASE)
sesion_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()
print("hey")