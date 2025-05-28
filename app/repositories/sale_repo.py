from sqlalchemy.orm import Session
from sqlalchemy import func, extract, and_
from typing import Optional, List
from datetime import date, datetime
from app.models.sale import Sale
from app.models.product import Product

class SaleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_summary(self):
        total_sales = self.db.query(func.sum(Sale.total_price)).scalar() or 0
        sale_count = self.db.query(func.count(Sale.id)).scalar() or 0
        return {
            "total_revenue": total_sales,
            "total_orders": sale_count
        }

    def get_sales_grouped_by(self, period: str):
        if period not in ["daily", "weekly", "monthly", "yearly"]:
            raise ValueError("Invalid period")

        date_format = {
            "daily": func.date_trunc("day", Sale.sale_date),
            "weekly": func.date_trunc("week", Sale.sale_date),
            "monthly": func.date_trunc("month", Sale.sale_date),
            "yearly": func.date_trunc("year", Sale.sale_date)
        }

        query = (
            self.db.query(date_format[period].label("period"), func.sum(Sale.total_price).label("total"))
            .group_by("period")
            .order_by("period")
        )

        return query.all()

    def filter_sales(
        self,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        product_id: Optional[int] = None,
        category: Optional[str] = None
    ) -> List[Sale]:
        query = self.db.query(Sale).join(Product)

        if start_date:
            query = query.filter(Sale.sale_date >= start_date)
        if end_date:
            query = query.filter(Sale.sale_date <= end_date)
        if product_id:
            query = query.filter(Sale.product_id == product_id)
        if category:
            query = query.filter(Product.category == category)

        return query.all()
