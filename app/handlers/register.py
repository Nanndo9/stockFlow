from fastapi import FastAPI, HTTPException
from app.exceptions.product import ProductNotFound, ProductNotUpdated
from app.exceptions.users import UserAlreadyExists, UserNotFound
from app.handlers.exception_handlers import (
    product_not_found_handler,
    http_exception_handler,
    product_not_updated_handler,
    user_already_exists_handler,
    user_not_found_handler,
)


def register_exception_handlers(app: FastAPI):

    app.add_exception_handler(ProductNotFound, product_not_found_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(ProductNotUpdated, product_not_updated_handler)
    app.add_exception_handler(UserNotFound, user_not_found_handler)
    app.add_exception_handler(UserAlreadyExists,user_already_exists_handler)