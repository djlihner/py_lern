from geom2d import *

l1 = [Point(3, 1), Point(1, 2), Point(2, 1)]

l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

print('ok')
print(l1)
print(l2)
