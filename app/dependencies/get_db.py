from sqlalchemy.orm import Session
from app.core.dataBase import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
