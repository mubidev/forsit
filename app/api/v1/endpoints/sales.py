from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import date
from app.repositories.sale_repo import SaleRepository
from app.schemas.sale import SaleResponse, SaleSummary, SalePeriodGroup
from app.core.database import get_db

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.get("/summary", response_model=SaleSummary)
def get_summary(db: Session = Depends(get_db)):
    repo = SaleRepository(db)
    return repo.get_summary()

@router.get("/by-period", response_model=List[SalePeriodGroup])
def get_sales_by_period(period: str = Query(..., enum=["daily", "weekly", "monthly", "yearly"]), db: Session = Depends(get_db)):
    repo = SaleRepository(db)
    try:
        return repo.get_sales_grouped_by(period)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/filter", response_model=List[SaleResponse])
def filter_sales(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    product_id: Optional[int] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    repo = SaleRepository(db)
    return repo.filter_sales(start_date, end_date, product_id, category)
