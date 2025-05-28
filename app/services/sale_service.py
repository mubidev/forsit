from fastapi import Depends
from sqlalchemy.orm import Session
from app.repositories.sale_repo import SaleRepository
from app.core.database import get_db
from app.schemas.sale import SalesSummaryResponse

class SaleService:
    def __init__(self, db: Session = Depends(get_db)):
        self.repo = SaleRepository(db)

    def get_summary(self) -> SalesSummaryResponse:
        summary = self.repo.get_summary()
        return SalesSummaryResponse(**summary)
