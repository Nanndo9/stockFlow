
from app.exceptions.users import UserAlreadyExists, UserNotFound
from app.repositories.userRepository import UserRepository
from app.schemas.UserSchema import UserCreate, UserRead, UserUpdate
from app.core.security import get_password_hash


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user_service(self, user: UserCreate) -> UserRead:

        userExists = self.user_repo.get_by_email(user.email)

        if userExists:
            raise UserAlreadyExists(user_email=user.email)
        
        user_data = user.model_dump(exclude={"password"})
        user_data["hashed_password"] = get_password_hash(user.password)

        create_user = self.user_repo.create_user(user_data)
        self.user_repo.db.commit()
        return UserRead.model_validate(create_user)
 