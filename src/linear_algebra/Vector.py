from array import array
import math
import itertools


class Vector:

    def __init__(self, components):
        self._components = array('d', components)

    def __repr__(self):
        components_str = ', '.join(str(x) for x in self._components)
        return '{}([{}])'.format(self.__class__.__name__, components_str)

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    ## double dispatch for x * y
    def __mul__(self, y):
        try:
            return Vector(x * y for x in self)
        except TypeError:
            return NotImplemented

    ## double dispatch for y * x - reversed
    def __rmul__(self, y):
        return self * y

    def __add__(self, other):  # <- - - - - - - - - - - new method
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0)
            return Vector(x + y for x, y in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):  # <- - - - - - - - - - - new method
        return self + other

if __name__ == '__main__':
    v1 = Vector([2, 4, 6])
    print(v1)

    v3 = Vector([10, 20, 30])
    x, y, z = v3  # tuple unpacking
    print(x, y, z)

    print('abs', abs(Vector([3,4])))

    for label, value in zip('xyz', v3):  # parallel iteration with zip
        print(label, '=', value)

    # scalar mul
    v5 = Vector([1, 2, 3, 4, 5])
    x = 11
    print(v5 * x)

    # duct typed
    try:
        res = Vector([10, 11, 12]) * 'spam'
    except TypeError as e:
        print(repr(e))
    else:
        print('OK! result:', res)

    # fractions
    from fractions import Fraction
    print(Fraction(1, 3) * Vector([10, 20, 30]))

    v1 = Vector([10, 11, 12, 13])
    v2 = Vector([32, 31, 30, 29])
    v3 = v1 + v2
    print(v3)  # --> Vector([42, 42, 42, 42])
    print(v3+Vector([100, 200]))