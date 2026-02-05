from datetime import datetime
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select

from app.db import init_db, get_session
from app.models import Task, TaskCreate, TaskRead, TaskUpdate

app = FastAPI(title="Task API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, session: Session = Depends(get_session)):
    task = Task(**payload.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.get("/tasks", response_model=List[TaskRead])
def list_tasks(
    limit: int = 20,
    offset: int = 0,
    session: Session = Depends(get_session),
):
    limit = max(1, min(limit, 100))  # clamp 1..100
    offset = max(0, offset)

    stmt = select(Task).offset(offset).limit(limit).order_by(Task.id)
    return session.exec(stmt).all()


@app.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(task, k, v)

    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return None
