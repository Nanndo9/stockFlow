from sqlalchemy import UUID


class UserNotFound(Exception):
    def __init__(self, user_id: UUID):
        self.user_id = user_id

        super().__init__(f"User not found: {user_id}")


class UserAlreadyExists(Exception):
    def __init__(self, user_email: str):
        self.user_email = user_email

        super().__init__(f"User with email '{user_email}' already exists.")
