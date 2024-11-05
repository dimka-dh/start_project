class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.price}, {self.category}"

    def __eq__(self, other):
        return self.name == other.name

class Shop:
    def __init__(self, file_name):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        existing_products = self.get_products()

        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
        file.close()

s1 = Shop('products.txt')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())