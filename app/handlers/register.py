from fastapi import FastAPI, HTTPException
from app.exceptions.product import ProductNotFound
from app.handlers.exception_handlers import (
    product_not_found_handler,
    http_exception_handler,
)

def register_exception_handlers(app: FastAPI):
  
    app.add_exception_handler(ProductNotFound, product_not_found_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
