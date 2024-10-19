class Figure:
    sides_count = 0  # количество сторон

    def __init__(self):
        self.__color = []  # список цветов в формате RGB
        self.__sides = []  # список сторон
        self.filled = False  # закрашенный, bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True  # возвращаем True, если цвет в диапазоне от 0 до 255 включительно

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  # если цвет в диапазоне от 0 до 255 включительно
            self.__color = [r, g, b]  # записываем цвет в формате RGB
        else:
            self.__color = self.__color

    def get_sides(self):
        return self.__sides

    def info(self):
        print(f'Figure: {self.__class__.__name__}, {self.get_color()}, {self.__sides}, {self.sides_count}')

    def __len__(self):
        if self.sides_count == 1:
            return int(int(*self.__sides) * 2 * 3.14)  # возвращаем периметр круга
        else:
            return sum(self.__sides)  # возвращаем периметр фигуры

    def set_sides(self, *new_sides):
        if len(list(new_sides)) != self.sides_count:  # если количество сторон не равно количеству сторон фигуры
            # проверяем если аттрибут __sides не существует, то создаем его
            self.__sides = [1] * self.sides_count if '_Figure__sides' not in str(dir(self)) else self.__sides
        else:
            self.__sides = list(new_sides)  # записываем стороны фигуры


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        r, g, b = color
        self.set_color(r, g, b)  # записываем цвет в формате RGB
        self.set_sides(*sides)  # записываем стороны фигуры
        self.__radius = self.get_sides()  # радиус круга

    def get_square(self):
        return int(*self.__radius) ** 2 * 3.14  # Возвращаем площадь круга


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        r, g, b = color
        self.set_color(r, g, b)  # записываем цвет в формате RGB
        self.set_sides(*sides)

    def get_square(self):
        a, b, c = self.get_sides()  # Стороны треугольника
        p = (a + b + c) / 2  # Полупериметр треугольника
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5  # Формула Герона для площади треугольника


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        r, g, b = color
        self.set_color(r, g, b)  # записываем цвет в формате RGB
        self.set_sides(*sides*12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


Circle((200, 200, 100), 10, 15, 6).info()  # т.к. сторона у круга всего 1, то его стороны будут - [1]
Triangle((200, 200, 100), 10, 6).info()  # т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Cube((200, 200, 100), 9).info()  # т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Cube((200, 200, 100), 9, 12).info()  # т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
print("_________")

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1), "  --- У вас тут ответ 15, но длина окружности 2пR равна 2*15*3.14=94")

# Проверка объёма (куба):
print(cube1.get_volume())

print("_________")

# Проверка площади (круга):
print(circle1.get_square())

triangle1 = Triangle((100, 210, 100), 10, 6, 5)
print(len(triangle1))
print(triangle1.get_square())