def add_everything_up(a, b):
    try:
        # Проверяем, если оба аргумента числа (int или float)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        # Проверяем, если оба аргумента строки
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        # Если типы разные (например, число и строка), вызываем TypeError
        else:
            raise TypeError
    except TypeError:
        # Обрабатываем TypeError и возвращаем строковое представление a и b
        return f"{a}{b}"

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456


# Вы отлично справились с решением задачи. Однако isinstance в блоке try немного бесмыслен. Вот рабочий код без него:
# def add_everything_up(a, b):
#   try:
#       return a + b
#   except TypeError:
#       return f"{a}{b}"
