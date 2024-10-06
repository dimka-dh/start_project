def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 11.89, 'text']
values_dict = {'a':"dict", 'b':True, 'c':[31, 58, 77]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['proba', 55.12]
print_params(*values_list_2, 42)
