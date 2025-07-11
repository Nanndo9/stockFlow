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
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def getByProductId(self, product: ProductBase) -> Products:
        db_product = Products(**product.model_dump())
        self.db.query(Products).all()
       
        return db_product
