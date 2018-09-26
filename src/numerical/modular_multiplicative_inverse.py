# https://numericalrecipes.wordpress.com/2009/03/20/modular-multiplicative-inverse/

def modInv1(a, m):
    """
    Computes the modular multiplicative inverse of a modulo m,
    using brute force
    """
    a %= m
    for x in range(1, m):
        if a * x % m == 1:
            return x
    return None


def extEuclideanAlg(a, b):
    """
    Computes a solution  to a x + b y = gcd(a,b), as well as gcd(a,b)
    http://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extEuclideanAlg(b, a % b)
        return y, x - y * (a // b), gcd


def modInvEuclid(a, m):
    """
    Computes the modular multiplicative inverse of a modulo m,
    using the extended Euclidean algorithm
    """
    x, y, gcd = extEuclideanAlg(a, m)
    if gcd == 1:
        return x % m
    else:
        return None


if __name__ == '__main__':
    print(modInv1(1234, 5))
    print(modInvEuclid(1234, 5))
    print(modInv1(1234, 56789))
    print(modInvEuclid(1234, 56789))
    print(modInvEuclid(3504, 385))
