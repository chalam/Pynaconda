import math


def karatsuba(x, y):
    """
    divide-and-conquer to multiply 2 numbers in Θ(N^(log2(3)) than the grade school algorithm Θ(N^2)
    if N-1024(2^10), 3^10 vs 2^10^2 17X speed-up with less multiplications
    instead of 4 mul, this uses 3-mul
    """
    sx = str(x)
    sy = str(y)
    nx = len(sx)
    ny = len(sy)
    if nx == 1 or ny == 1:
        r = int(x) * int(y)
        return r
    n = nx
    if nx > ny:
        sy = sy.rjust(nx, '0')
        n = nx
    elif ny > nx:
        sx = sx.rjust(ny, '0')
        n = ny
    m = n % 2
    offset = 0
    if m != 0:
        n += 1
        offset = 1
    floor = int(math.floor(n / 2)) - offset
    ceil = int(math.ceil(n / 2)) - offset
    a = sx[0:floor]
    b = sx[ceil:n]
    c = sy[0:floor]
    d = sy[ceil:n]
    # T
    r = ((10 ** n) * karatsuba(a, c)) + ((10 ** (n / 2)) * (karatsuba(a, d) + karatsuba(b, c))) + karatsuba(b, d)
    return r

assert karatsuba(12345, 6789) == 12345 * 6789
assert karatsuba(773920, 583922303) == 773920 * 583922303
x = 5313969797022876007865453254137711291618937695170868966548357976313192691870262523766483684170857804
y = 9783483294082441361180615595894143546512317591170502530626606255574218864396333893954928230682223373
print(karatsuba(x, y))