from geom2d import *

# сконструировали два объекта
a = Point(0, 0)
b = Point(3, 4)
# вызвали метод
print(a.distance(b))
# убедилиись, что работает операция сравнения
print(a == b)
print(a == Point(0, 0))