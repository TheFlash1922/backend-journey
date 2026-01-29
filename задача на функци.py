from datetime import datetime

def log_error(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("errors.log", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Ошибка: {message}\n")