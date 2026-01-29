def safe_read_file(filename):
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Файл не существует"
    except Exception:
        return "Ошибка при чтении"