from fastapi import FastAPI
from pydantic import BaseModel, Field
import json
import os

app = FastAPI()

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, strip_whitespace=True)
    completed: bool

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
    save_tasks(tasks)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    task_found = False
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            task_found = True
            break
    if not task_found:
        return {"error": "Задача не найдена"}
    save_tasks(tasks)
    return {"message": f"Задача {task_id} удалена"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    global tasks
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["completed"] = task_update.completed
            save_tasks(tasks)
            return task
    return {"error": "Задача не найдена"}

@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в backend-journey!",
        "docs_url": "/docs"
    }