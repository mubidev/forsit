from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    sale_date: datetime

    class Config:
        orm_mode = True

class SaleSummary(BaseModel):
    total_revenue: float
    total_orders: int

class SalePeriodGroup(BaseModel):
    period: datetime
    total: float
