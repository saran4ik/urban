from os.path import exists as ex
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):  # получение списка товаров из файла
        if ex(self.__file_name):  # проверка наличия файла
            file = open(self.__file_name, 'r')
            products = file.read()
            file.close()
            return products
        else:
            return 'Файл не существует'

    def add(self, *prod):  # добавление нескольких товаров в файл
        if ex(self.__file_name):  # проверка наличия файла
            pass
        else:
            file = open(self.__file_name, 'w')  # если файла нет, то создаем файл
            file.close()
        file = open(self.__file_name, 'r+')
        products = file.read()
        for p in prod:
            if p.name not in products:  # проверка наличия продукта по имени в файле
                file.write(f'{p}\n')
            else:
                print(f'Продукт {p} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

