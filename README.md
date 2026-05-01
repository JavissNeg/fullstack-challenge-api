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
- GET /api/v1/flights/analytics/top-airport
- GET /api/v1/flights/analytics/top-airline
- GET /api/v1/flights/analytics/top-day
- GET /api/v1/flights/analytics/airlines-over-two

### Stack Analytics
- GET /api/v1/stack/analytics/stats
- GET /api/v1/stack/analytics/highest-reputation
- GET /api/v1/stack/analytics/lowest-views
- GET /api/v1/stack/analytics/oldest
- GET /api/v1/stack/analytics/newest

---

## 🔐 Notes
- Swagger: /docs
- HTTPS enabled (self-signed cert in Docker)
- Alembic for DB migrations
"""