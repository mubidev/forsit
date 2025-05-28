from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product_data: ProductCreate) -> Product:
        product = Product(**product_data.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def get_all_products(self) -> List[Product]:
        return self.db.query(Product).all()

    def get_low_stock_products(self) -> List[Product]:
        return self.db.query(Product).filter(Product.stock_quantity <= Product.low_stock_threshold).all()

    def update_stock_quantity(self, product_id: int, new_quantity: int) -> Optional[Product]:
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            product.stock_quantity = new_quantity
            self.db.commit()
            self.db.refresh(product)
        return product
