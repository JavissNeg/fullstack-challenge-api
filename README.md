# Mecate API

FastAPI project for flights data management.

## Setup

### Prerequisites
- Docker & Docker Compose (or Podman)
- Python 3.11+

### Development (Local)

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Setup environment:**
```bash
cp .env.example .env
```

3. **Start PostgreSQL:**
```bash
docker-compose up postgres -d
```

4. **Run migrations:**
```bash
alembic upgrade head
```

5. **Seed database:**
```bash
python -c 'from src.core.init_db import seed_data; seed_data()'
```

6. **Start API:**
```bash
uvicorn src.main:app --reload
```

API available at: http://localhost:8000

---

### Docker

**Build and run:**
```bash
docker-compose up --build
```

**Down containers:**
```bash
docker-compose down
```

**Reset database (clear volume):**
```bash
docker-compose down -v
docker-compose up --build
```

---

### Database Migrations

**Create migration:**
```bash
alembic revision --autogenerate -m "description"
```

**Apply migrations:**
```bash
alembic upgrade head
```

**Rollback migration:**
```bash
alembic downgrade -1
```

**In Docker:**
```bash
docker-compose run backend alembic revision --autogenerate -m "description"
docker-compose run backend alembic upgrade head
```

---

### API Endpoints

- `GET /api/v1/health` - Health check with DB connection status
- `GET /api/v1/flights/airlines` - List airlines
- `GET /api/v1/flights/airports` - List airports
- `GET /api/v1/flights/flights` - List flights

---

### Project Structure

```
src/
├── core/
│   ├── config.py          # Settings
│   ├── database.py        # DB engine & session
│   ├── init_db.py         # DB initialization
│   ├── logging.py         # Logger setup
│   ├── router_registry.py # Auto-register routers
│   └── seed.py            # Seed data
├── modules/
│   ├── flights/
│   │   ├── models.py      # SQLAlchemy models
│   │   └── router.py      # FastAPI routes
│   └── health/
│       └── router.py      # Health check
├── main.py                # FastAPI app entry
└── models.py              # Centralized model exports
```
