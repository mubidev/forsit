# 🛒 E-Commerce Admin Dashboard API (FastAPI)

A backend API built with **FastAPI** and **PostgreSQL** to power an admin dashboard for e-commerce managers. It provides endpoints for sales analysis, product registration, and inventory management.

---

##  Features

###  Sales Insights
- Revenue breakdown by day, week, month, and year.
- Filter sales by date range, product, or category.
- Period-over-period comparisons.

###  Inventory Management
- View current stock status.
- Automatic low stock alerts.
- Update inventory levels.
- Automatically deduct inventory on product sale.

###  Product Management
- Register new products with name, category, and price.

---

##  Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Validation**: Pydantic
- **Project Structure**: Repository Pattern

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd forsit
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
alembic upgrade head
```
```
Note: Make sure PostgreSQL is running and your DATABASE_URL is correctly set in app/core/config.py or .env
```

### 5. Start the API Server

```bash
uvicorn app.main:app --reload
```
```
Access Swagger UI at: http://localhost:8000/docs
```

##  API Endpoints Overview

###  `/products/`
- `POST /products/` – Register a new product
- `GET /products/` – List all products

###  `/sales/`
- `POST /sales/` – Create a new sale and update inventory
- `GET /sales/summary/` – Get sales and revenue summary (daily, weekly, monthly, yearly)
- `GET /sales/filter/` – Filter sales by date range, product, or category

###  `/inventory/`
- `GET /inventory/` – View current inventory status
- `GET /inventory/low-stock/` – List products with low stock
- `PUT /inventory/update/` – Manually update inventory levels

---

## Demo Data

To populate the database with sample products and sales data:

```bash
python app/demo/populate_demo_data.py
