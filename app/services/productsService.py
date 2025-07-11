from app.repositories.productRepository import ProductRepository
from app.schemas.productSchema import ProductCreate, ProductRead


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product_service(self, product: ProductCreate) -> ProductRead:
        db_product = self.product_repo.create(product)
        
        return ProductRead.model_validate(db_product)

    def getByProductId(self, product: ProductCreate) -> ProductRead:
        db_product = self.product_repo.getByProductId(product)
        return ProductRead.model_validate(db_product)
