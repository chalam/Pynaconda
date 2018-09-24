from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], verbose=False)
print(Point)

p = Point(11, y=22)
print(p)
print(p._fields)
print(p.x, p.y, p[0], p[1])

p2 = Point._make([33, 44])
print(p2)

p3 = Point._make([p.x + p2.x, p.y + p2.y])
print(p3)
print(p3._asdict())

d = {'x': 55., 'y': 66}
p4 = Point(**d) # To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):
print(p4)

# *args = unpack list of args
# **args = unpack dict of args
