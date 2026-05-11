"""
Sanos y Salvos — Geolocation Microservice
Handles geospatial data processing and map interfaces.
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text

from app.api.routes import router
from app.config import Base, engine
from app.models import location

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("geo-service")

def init_database():
    """Create PostGIS extension, service schema and tables when running fresh."""
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS geo_service"))
    Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Sanos y Salvos — Geolocalización",
    description="Microservicio de geolocalización con PostGIS para mapeo interactivo",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "geolocation-service"}
