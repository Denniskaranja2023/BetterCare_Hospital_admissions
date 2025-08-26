from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine= create_engine("sqlite:///hospital_admissions.db")
Session= sessionmaker(bind=engine)
session= Session()
Base = declarative_base()