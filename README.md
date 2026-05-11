# Sanos y Salvos - API Geolocation

API de geolocalizacion para registrar ubicaciones, buscar reportes cercanos y generar datos para mapas.

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL/PostGIS
- Docker

## Variables de entorno

Copia `.env.example` como `.env` y ajusta los valores.

## Ejecucion local

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

## Docker

```bash
docker build -t sanos-salvos-api-geolocation .
docker run --env-file .env -p 8002:8002 sanos-salvos-api-geolocation
```

## Endpoints principales

- `POST /api/geo/locations`
- `GET /api/geo/reports`
- `GET /api/geo/nearby`
- `GET /api/geo/heatmap`
- `GET /api/geo/zones`
