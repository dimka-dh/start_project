first = 42
second = 69
third = 42

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)