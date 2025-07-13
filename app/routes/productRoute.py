from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies.services import get_product_service
from app.schemas.productSchema import ProductCreate, ProductRead, ProductUpdate
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
    db_product = product_service.create_product_service(product)
    return db_product


@router.get("/list", response_model=list[ProductRead], status_code=status.HTTP_200_OK)
def list_all_products(product_service: ProductService = Depends(get_product_service)):
    db_product = product_service.get_all_product()
    return db_product


@router.get("/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK)
def get_by_id(
    product_id: uuid.UUID,
    product_service: ProductService = Depends(get_product_service),
):
    db_product = product_service.get_by_id(product_id)
    return db_product


@router.patch(
    "/{product_id}", response_model=ProductRead, status_code=status.HTTP_200_OK
)
def update_product(
    product_id: uuid.UUID,
    product: ProductUpdate,
    product_service: ProductService = Depends(get_product_service),
):
    db_product = product_service.update_product(product, product_id)
    return db_product


@router.delete(
    "/{product_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(
    product_id: uuid.UUID,
    product_service: ProductService = Depends(get_product_service),
):
    product_service.delete_product(product_id)
