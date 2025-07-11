from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.services import get_product_service
from app.schemas.productSchema import ProductCreate, ProductRead
from app.services.productsService import ProductService
import uuid

router = APIRouter(
    prefix="/products", tags=["Products"], responses={404: {"description": "Not Found"}}
)


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_new_product(
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service),
):
    """Criar um novo produto"""
    db_product = product_service.create_product_service(product)
    return db_product
