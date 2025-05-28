from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from app.models.base import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    sale_date = Column(DateTime)
