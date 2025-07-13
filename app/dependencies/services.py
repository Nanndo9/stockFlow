from app.dependencies.get_db import get_db
from app.repositories.userRepository import UserRepository
from app.services.productsService import ProductService
from app.repositories.productRepository import ProductRepository
from sqlalchemy.orm import Session
from fastapi import Depends

from app.services.userService import UserService


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    product_repo = ProductRepository(db)
    return ProductService(product_repo)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repo = UserRepository(db)

    return UserService(user_repo)
