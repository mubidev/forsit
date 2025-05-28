from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.repositories.product_repo import ProductRepository
from app.core.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    created_product = repo.create_product(product)
    return created_product
