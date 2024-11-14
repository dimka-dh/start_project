def is_prime(func):
    # Декоратор
    def wrapper(*args, **kwargs):
        # Получаем результат от функции, к которой применяется декоратор
        result = func(*args, **kwargs)

        # Проверка, является ли число простым
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        # Возвращаем результат работы функции
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    # Функция складывает 3 числа
    return a + b + c


# Пример вызова
result = sum_three(2, 3, 6)
print(result)
