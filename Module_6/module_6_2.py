class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        if color.lower() in self.__COLOR_VARIANTS:
            self.__color = color
        else:
            self.__color = 'default'

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)
        self.passengers_limit = self.__PASSENGERS_LIMIT


vehicle1 = Sedan('Семен', 'Toyota Mark II', 'black', 500)

# Изначальные свойства
vehicle1.print_info()
print()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Yellow')
vehicle1.set_color('RED')
vehicle1.owner = 'Антошка'
print()

# Проверяем что поменялось
vehicle1.print_info()
