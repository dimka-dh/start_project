def gen_pass(n):
    if n < 3 or n > 20:
        return "Ошибка: число n должно быть в диапазоне от 3 до 20."
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += f"{i}{j}"
    return password

result1 = gen_pass(9)
result2 = gen_pass(11)
result3 = gen_pass(15)
result4 = gen_pass(21)

print(result1)
print(result2)
print(result3)
print(result4)

