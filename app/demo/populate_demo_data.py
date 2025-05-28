import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.product import Product
from app.models.sale import Sale

CATEGORIES = ["Electronics", "Books", "Home", "Clothing", "Toys"]

PRODUCTS = [
    {"name": "Wireless Mouse", "category": "Electronics", "price": 25.99},
    {"name": "Bluetooth Headphones", "category": "Electronics", "price": 59.99},
    {"name": "Python Programming Book", "category": "Books", "price": 39.99},
    {"name": "Vacuum Cleaner", "category": "Home", "price": 89.99},
    {"name": "Winter Jacket", "category": "Clothing", "price": 120.00},
    {"name": "Building Blocks Toy", "category": "Toys", "price": 19.99},
    {"name": "LED Desk Lamp", "category": "Home", "price": 29.99},
    {"name": "Gaming Keyboard", "category": "Electronics", "price": 45.00},
]

def populate_products(db: Session):
    for prod in PRODUCTS:
        product = Product(name=prod["name"], category=prod["category"], price=prod["price"])
        db.add(product)
    db.commit()
    print("Products added.")

def populate_sales(db: Session):
    products = db.query(Product).all()
    for _ in range(100):  # Create 100 sales
        product = random.choice(products)
        quantity = random.randint(1, 5)
        sale_date = datetime.utcnow() - timedelta(days=random.randint(0, 365))
        total_price = round(product.price * quantity, 2)

        sale = Sale(
            product_id=product.id,
            quantity=quantity,
            total_price=total_price,
            sale_date=sale_date
        )
        db.add(sale)
    db.commit()
    print("Sales added.")

def run():
    db = SessionLocal()
    try:
        populate_products(db)
        populate_sales(db)
    finally:
        db.close()

if __name__ == "__main__":
    run()
