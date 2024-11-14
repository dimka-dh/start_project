def all_variants(text):
    # Внешний цикл - определяет длину подпоследовательности
    for length in range(1, len(text) + 1):
        # Внутренний цикл - создает все подпоследовательности текущей длины
        for start in range(len(text) - length + 1):
            yield text[start:start + length]

# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)
