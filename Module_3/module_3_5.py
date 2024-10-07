def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number) if str_number != '0' else 1
    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(50810)
print(result)
print(result2)