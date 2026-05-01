"""
# ✈️ Challenge API

FastAPI service for flight data management with analytics modules.

---

## 🚀 Base URLs
- https://localhost:8443

---

## ⚙️ Setup

docker-compose up --build

---

## 🗄️ Migrations
alembic upgrade head

---

## 📡 API Modules

### Health
- GET /api/v1/health

### Flights Analytics
- GET /api/v1/flights/top-airport
- GET /api/v1/flights/top-airline
- GET /api/v1/flights/top-day
- GET /api/v1/flights/airlines-over-two

### Stack Analytics
- GET /api/v1/stack/stats
- GET /api/v1/stack/highest-reputation
- GET /api/v1/stack/lowest-views
- GET /api/v1/stack/oldest
- GET /api/v1/stack/newest

---

## 🔐 Notes
- Swagger: /docs
- HTTPS enabled (self-signed cert in Docker)
- Alembic for DB migrations
"""