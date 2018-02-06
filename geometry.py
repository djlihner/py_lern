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


# сконструировали два объекта
a = Point(0, 0)
b = Point(3, 4)
# вызвали метод
print(a.distance(b))
# убедилиись, что работает операция сравнения
print(a == b)
print(a == Point(0, 0))
