from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Файл для хранения задач
TASKS_FILE = "tasks.json"

# Загрузка задач из файла (или создание пустого списка)
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Сохранение задач в файл
def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# Модель для создания задачи
class TaskCreate(BaseModel):
    title: str

# Загружаем задачи при старте
tasks = load_tasks()

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Задача не найдена"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_id = max(t["id"] for t in tasks) + 1 if tasks else 1
    new_task = {"id": new_id, "title": task.title, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)  # ← сохраняем в файл!
    return new_task