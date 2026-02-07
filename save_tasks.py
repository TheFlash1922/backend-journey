import json
tasks = [
    {"id":1,"title":"Выучить Python","completed":False},
    {"id":2,"title":"Создать API","completed":True},
    {"id":3,"title":"Изучить JSON","completed":False}
]
with open("tasks_backup.json", "w", encoding="utf-8") as f:
    json.dump(tasks,f,ensure_ascii=False, indent=2)
    
