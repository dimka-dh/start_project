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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 4)
h3 = House('СНТ Оленёво', 13)
h1.go_to(4)
h2.go_to(4)
h3.go_to(14)
