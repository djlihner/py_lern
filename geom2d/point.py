from math import sqrt


class Point:  # класс
    def __init__(self, _x, _y):  # конструктор
        self.x = _x
        self.y = _y

    def distance(self, p2):  # метод
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx * dx + dy * dy)

    def __eq__(self, other): # переопределили операцию сранения
        return self.x == other.x and self.y == other.y