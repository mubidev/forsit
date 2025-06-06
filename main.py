from fastapi import FastAPI
from app.api.v1.api_router import api_router

app = FastAPI(title="E-Commerce Dashboard API")

app.include_router(api_router, prefix="/api/v1")
