from sqlalchemy.orm import Session
from typing import Optional
import uuid

from app.entities.products import Products
from app.schemas.productSchema import ProductBase


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductBase) -> Products:
        db_product = Products(**product.model_dump())
        self.db.add(db_product)
        self.db.refresh(db_product)
        return db_product

    def get_all_product(self) -> list[Products]:
        result_all_products = self.db.query(Products).all()

        return result_all_products

    def get_by_id(self, id: uuid.UUID) -> Optional[Products]:
        get_product_id = self.db.query(Products).get(id)
        return get_product_id

    def get_by_sku(self, sku: str) -> Optional[Products]:
        get_product_sku = self.db.query(Products).filter(Products.sku == sku).first()
        return get_product_sku
