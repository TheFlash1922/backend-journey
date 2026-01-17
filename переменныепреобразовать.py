price_str = "19.99"
quantity_str = "3"

# Преобразуем СТРОКИ в числа
price = float(price_str)      # "19.99" → 19.99
quantity = int(quantity_str)  # "3" → 3

total = price * quantity
print(total)  # → 59.97