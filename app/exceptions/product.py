from sqlalchemy import UUID


class ProductNotFound(Exception):
    def __init__(self, product_id: UUID):
        self.product_id = product_id

        super().__init__(f"Product not found: {product_id}")


class ProductNotUpdated(Exception):
    def __init__(self, product_id: UUID, reason: str = "unknown reason"):
        self.product_id = product_id
        self.reason = reason

        super().__init__(
            f"Product with ID '{product_id}' could not be updated: {reason}"
        )
