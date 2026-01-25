# 1. Читаем содержимое
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 2. Добавляем строку
content += "\n— Конец заметки"

# 3. Сохраняем обратно
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write(content)