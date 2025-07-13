from sqlalchemy.orm import Session
from typing import Optional, Dict, Any
import uuid

from app.entities.users import Users
from app.schemas.UserSchema import UserBase, UserRead


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: Dict[str, Any]) -> Users:
        db_user = Users(**user_data)
        self.db.add(db_user)
        self.db.flush()
        self.db.refresh(db_user)
        return db_user

    def get_by_id(self, user_id: uuid.UUID) -> Optional[Users]:
        get_user = self.db.get(user_id)

        return get_user

    def get_by_email(self, email: str) -> Optional[Users]:
        get_email = self.db.query(Users).filter(Users.email == email).first()

        return get_email
