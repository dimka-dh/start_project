def apply_all_func(int_list, *functions):
    results = {}  # создаём пустой словарь для хранения результатов

    # Перебираем все переданные функции
    for func in functions:
        # Применяем функцию к int_list и сохраняем результат в словарь под именем функции
        results[func.__name__] = func(int_list)

    return results  # возвращаем словарь с результатами


# Пример использования функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
