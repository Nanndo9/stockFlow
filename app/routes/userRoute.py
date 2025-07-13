from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.services import get_user_service
from app.schemas.UserSchema import UserCreate, UserRead, UserUpdate
from app.services.userService import UserService
import uuid


router = APIRouter(
    prefix="/user", tags=["Users"], responses={404: {"description": "Not Found"}}
)


@router.post("/",response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_new_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
):
    db_user = user_service.create_user_service(user)

    return db_user
