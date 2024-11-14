# Функция personal_sum
def personal_sum(numbers):
    result = 0  # для суммы чисел
    incorrect_data = 0  # для подсчета некорректных данных

    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


# Функция calculate_average
def calculate_average(numbers):
    try:
        total, incorrect_data = personal_sum(numbers)  # вызов функции для подсчета суммы
        count = len(numbers) - incorrect_data  # общее количество чисел без некорректных данных
        return total / count  # расчет среднего значения
    except ZeroDivisionError:
        return 0  # если деление на 0, вернем 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Тестовые вызовы функции calculate_average с разными входными данными
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
