from fastapi.testclient import TestClient
from main import app

def test_create_task():
    client = TestClient(app)
    response = client.post("/tasks", json={"title": "Купить хлеб"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Купить хлеб"
    assert data["completed"] == False
    assert "id" in data

def test_get_tasks():
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    # Проверим, что хотя бы одна задача есть (из предыдущего теста)
    assert len(tasks) >= 1

def test_update_task():
    client = TestClient(app)
    # Сначала создадим задачу
    create_response = client.post("/tasks", json={"title": "Старое название"})
    task_id = create_response.json()["id"]
    
    # Обновим её
    update_response = client.put(f"/tasks/{task_id}", json={
        "title": "Новое название",
        "completed": True
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Новое название"
    assert data["completed"] == True

def test_delete_task():
    client = TestClient(app)
    # Создадим задачу
    create_response = client.post("/tasks", json={"title": "На удаление"})
    task_id = create_response.json()["id"]
    
    # Удалим её
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Задача {task_id} удалена"
    
    # Убедимся, что её больше нет
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
