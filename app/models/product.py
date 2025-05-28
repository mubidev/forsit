from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    category = Column(String(100), index=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    low_stock_threshold = Column(Integer, default=10)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def is_low_stock(self) -> bool:
        return self.stock_quantity <= self.low_stock_threshold
