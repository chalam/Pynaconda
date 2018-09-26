def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd2(a, b):
    if b == 0:
        return a
    return gcd2(b, a%b)

def extEuclideanAlg(a, b):
    """
    Computes a solution  to a x + b y = gcd(a,b), as well as gcd(a,b)
    http://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
     ax + by = gcd(a,b)
     since x is the modular multiplicative inverse of a modulo b,
     and y is the modular multiplicative inverse of b modulo a.
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extEuclideanAlg(b, a % b)
        return y, x - y * (a // b), gcd

if __name__ == '__main__':
    print(gcd(30, 18))
    print(gcd2(30, 18))
    print(gcd(18, 30))
    import math
    print(math.gcd(18, 30))
    x, y, gcd = extEuclideanAlg(18, 30)
    print(x, y, gcd)
    assert (x, y, gcd) == (2, -1, 6)
    assert 18*x + 30*y == gcd