first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для вычисления разницы длин строк, если длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях, без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример вывода результатов
print(list(first_result))     # Преобразуем генератор в список для вывода результата
print(list(second_result))    # Преобразуем генератор в список для вывода результата
