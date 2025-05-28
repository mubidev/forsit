from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductResponse
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/", response_model=List[ProductResponse])
def get_inventory(db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    return repo.get_all_products()

@router.get("/low-stock", response_model=List[ProductResponse])
def get_low_stock_inventory(db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    return repo.get_low_stock_products()

@router.patch("/{product_id}", response_model=ProductResponse)
def update_stock(product_id: int, quantity: int, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    updated_product = repo.update_stock_quantity(product_id, quantity)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
