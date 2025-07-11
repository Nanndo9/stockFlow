
from sqlalchemy import UUID


class ProductNotFound(Exception):
    def __init__(self, product_id: UUID):
        self.product_id = product_id
        
        super().__init__(f"Product not found: {product_id}")
