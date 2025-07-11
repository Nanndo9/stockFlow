from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass