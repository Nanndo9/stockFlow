import uuid
from fastapi import HTTPException, status
from app.exceptions.product import ProductNotFound
from app.repositories.productRepository import ProductRepository
from app.schemas.productSchema import ProductCreate, ProductRead


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product_service(self, product: ProductCreate) -> ProductRead:

        product_exists = self.product_repo.get_by_sku(product.sku)
        
        if product_exists:
            
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Product with Sku '{product.sku}'  already exists.",
            )

        db_product = self.product_repo.create(product)
        self.product_repo.db.commit()

        return ProductRead.model_validate(db_product)

    def get_all_product(self) -> list[ProductRead]:
        db_product_list = self.product_repo.get_all_product()

        return [ProductRead.model_validate(product) for product in db_product_list]

    def get_by_id(self, product_id: uuid.UUID) -> ProductRead:
        
        db_product_by_id = self.product_repo.get_by_id(product_id)
        
        if not db_product_by_id:
            raise ProductNotFound(product_id=product_id)
        
        return ProductRead.model_validate(db_product_by_id)
