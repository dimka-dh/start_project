class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'В "{self.name}" всего {self.number_of_floors} этажей')
        if 1 < new_floor < (self.number_of_floors + 1):
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Горский', 8)
h2 = House('Домик в деревне', 18)
h3 = House('СНТ Оленёво', 13)

# __str__
print(h1)
print(h2)
print(h3)

# __eq__
print(h1 == h2)

# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

# Сравнения
print(h1 > h2)
print(h2 >= h3)
print(h1 < h3)
print(h1 <= h2)
print(h2 != h3)


# h1.go_to(4)
# h2.go_to(4)
# h3.go_to(14)
# print(h1)
# print(h2)
# print(h3)
# print(len(h1))
# print(len(h2))
# print(len(h3))
