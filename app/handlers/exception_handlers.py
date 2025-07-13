from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.exceptions.product import ProductNotFound, ProductNotUpdated
from app.exceptions.users import UserAlreadyExists, UserNotFound


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "status_code": exc.status_code,
                "detail": exc.detail,
                "path": str(request.url.path),
                "method": request.method,
            }
        },
    )


async def product_not_found_handler(request: Request, exc: ProductNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "status_code": status.HTTP_404_NOT_FOUND,
                "detail": f"Product with ID '{exc.product_id}' not found.",
                "path": str(request.url.path),
                "method": request.method,
            }
        },
    )


async def product_not_updated_handler(request: Request, exc: ProductNotUpdated):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "detail": f"Could not update product with ID '{exc.product_id}': {exc.reason}",
                "path": str(request.url.path),
                "method": request.method,
            }
        },
    )


async def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "status_code": status.HTTP_404_NOT_FOUND,
                "detail": f"User with ID '{exc.user_id}' not found.",
                "path": str(request.url.path),
                "method": request.method,
            }
        },
    )


async def user_already_exists_handler(request: Request, exc: UserAlreadyExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": {
                "status_code": status.HTTP_409_CONFLICT,
                "detail": f"User with email '{exc.user_email}' already exists.",
                "path": str(request.url.path),
                "method": request.method,
            }
        },
    )
