# task-api (Python + FastAPI)

A small REST API written in **Python**, built with **FastAPI**.
Designed as a simple, understandable backend project with clean structure and explicit behavior.

Includes:

- RESTful CRUD endpoints
- SQLite persistence
- Pydantic models (validation + serialization)
- Clear separation of concerns (models / db / routes)
- Minimal setup (no Docker, no auth, no fluff)

## Requirements

- Windows / macOS / Linux
- Python **3.12+**
- `pip`
- Virtual environment recommended

## Setup

From the repo root:


```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Run

From the repo root:

```bash
uvicorn app.main:app --reload
```

## Test

From the repo root:

```bash
pytest
```

## API will be available at:

- http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

## Project Layout

```text
task-api/
├─ app/
│  ├─ main.py        # FastAPI app instance + route definitions
│  ├─ db.py          # Database engine, session handling, startup init
│  ├─ models.py      # SQLModel / Pydantic models (Task schemas)
│  └─ __init__.py
│
├─ tests/
│  └─ test_tasks.py  # Basic CRUD endpoint tests
│
├─ .gitignore
└─ README.md
```

### Task API (Quick Reference)

| Method | Endpoint | Description | Returns |
|------|---------|-------------|---------|
| `GET` | `/tasks` | Retrieve all tasks | `list[TaskRead]` |
| `GET` | `/tasks/{id}` | Retrieve a task by ID | `TaskRead` |
| `POST` | `/tasks` | Create a new task | `TaskRead` |
| `PUT` | `/tasks/{id}` | Update an existing task | `TaskRead` |
| `DELETE` | `/tasks/{id}` | Delete a task | `204 No Content` |

### Task Schema

```json
{
  "id": 1,
  "title": "Example task",
  "description": "Optional description",
  "is_done": false,
  "created_at": "2026-02-05T18:10:00Z",
  "updated_at": "2026-02-05T18:10:00Z"
}
```

#### Notes
- Uses SQLite (file-based DB, no setup required)
- Validation handled via Pydantic / SQLModel
- No authentication (intentionally simple)
- Designed as a learning / portfolio project, not production-ready

## Storage format

All users are stored in one JSON file:

- storage.json – current DB  (`storage.json`)
- backupfile.json – last corrupt JSON backup (if corruption detected)  (`backupfile.json`)

## Version history
#### v0.1.0
- Initial REST API
- CRUD endpoints for tasks
- SQLite persistence
#### v0.2.0
- Validation improvements
- Test coverage added

## Authors
### Hassan (@hazi7k)
### GitHub: https://github.com/hazi7k
