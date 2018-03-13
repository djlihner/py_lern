from geom2d import *

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]


def x(p):
    return p.x


def y(p):
    return p.y


l2 = sorted(l1, key=x)

print('ok')
print(l1)
print(l2)
