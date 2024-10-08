from packages.fake_math import divide as fake_result
from packages.true_math import divide as true_result

result1 = fake_result(69, 23)
result2 = fake_result(8, 0)
result3 = true_result(45, 5)
result4 = true_result(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)