from fastapi import FastAPI
from sqlalchemy import Column, SmallInteger, Text,String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    EMP_ID = Column(SmallInteger, primary_key=True)
    FIRST_NAME = Column(String(255))
    LAST_NAME = Column(String(255))
    GENDER = Column(String(255))
    AGE = Column(SmallInteger)
    EMAIL = Column(String(255))
    PHONE_NR = Column(String(255))
    EDUCATION = Column(String(255))
    MARITAL_STAT = Column(String(255))
    NR_OF_CHILDREN = Column(SmallInteger)


from sqlalchemy import create_engine
engine = create_engine("sqlite:///testdb.db")


