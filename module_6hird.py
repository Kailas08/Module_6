class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def __is_valid_color(self, r, g, b):
        if all(0 <= c <= 255 for c in (r, g, b)):
            return True
        return False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        if all(isinstance(s, int) and s > 0 for s in new_sides) and len(new_sides) == self.sides_count:
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, radius, color, filled):
        super().__init__([2 * radius], color, filled)
        self.__radius = radius

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, height, color, filled):
        super().__init__(sides, color, filled)
        self.__height = height

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides, color, filled):
        super().__init__([sides] * 12, color, filled)
        Figure.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle(10, (200, 200, 100), True) # (Цвет, стороны)
cube1 = Cube(6, (222, 35, 130), True)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())