from __future__ import annotations
# === 1. ИМПОРТЫ: подключаем нужные инструменты ===
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import ConfigDict


# === 2. КОНФИГУРАЦИЯ: настройка приложения и базы данных ===
app = FastAPI(title="Todo API")

# Подключение к SQLite
engine = create_engine("sqlite:///./tasks.db")
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# === 3. МОДЕЛЬ БАЗЫ ДАННЫХ: как выглядит задача в БД ===
class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Создаём таблицы при запуске
Base.metadata.create_all(bind=engine)


# === 4. МОДЕЛИ ДАННЫХ (Pydantic): как выглядят данные от клиента ===
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    completed: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    model_config = ConfigDict(from_attributes=True)

# === 5. ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ: получение сессии БД ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# === 6. МАРШРУТЫ: точки входа в API ===

@app.get("/")
def root():
    return {"message": "Welcome to Todo API!", "docs_url": "/docs"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    """Получить все задачи"""
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    db.close()
    return tasks

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    """Создать новую задачу"""
    db = SessionLocal()
    db_task = TaskDB(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    """Обновить задачу по ID"""
    db = SessionLocal()
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    db_task.title = task_update.title
    db_task.completed = task_update.completed
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Удалить задачу по ID"""
    db = SessionLocal()
    db_task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    db.delete(db_task)
    db.commit()
    db.close()
    return {"message": f"Задача {task_id} удалена"}

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    db=SessionLocal()
    db_task=db.query(TaskDB).filter(TaskDB.id==task_id).first()
    db.close()
    if not db_task:
        raise HTTPException(status_code=404,detail="Задача не найдена")
    return db_task

