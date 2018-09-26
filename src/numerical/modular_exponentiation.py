# https://numericalrecipes.wordpress.com/2009/03/20/modular-exponentiation/
# a^b (mod m)
# the remainder of a to the power of b, divided by m.
import math


def modExp1(a, b, m):
    """
    Computes a to the power b, modulo m, directly
    """
    return a ** b % m


def modExp2(a, b, m):
    """
    Computes a to the power b, modulo m, a little less directly
    """
    return (a % m) ** b % m


def modExp3(a, b, m):
    """
    Computes a to the power b, modulo m, by iterative multiplication
    """
    ret = 1
    a %= m
    while b:
        ret *= a
        ret %= m
        b -= 1
    return ret


def modExp(a, b, m):
    """
    Computes a to the power b, modulo m, using binary exponentiation
    http://www.johndcook.com/blog/2008/12/10/fast-exponentiation/
    http://en.wikipedia.org/wiki/Binary_exponentiation
    when asked to compute ab, check if b is even,
    in which case we will compute it as the square of a^b/2.
    If b is odd, we will compute it as a·a^b-1.
     2 log2(n) multiplications
    """
    a %= m
    ret = None
    if b == 0:
        ret = 1
    elif b % 2: # square self and multiply by a
        ret = a * modExp(a, b - 1, m)
    else:       # square self
        ret = modExp(a, b // 2, m)
        ret *= ret
    return ret % m


if __name__ == '__main__':
    print(modExp1(1234, 5678, 90))
    print(modExp2(1234, 5678, 90))
    print(modExp3(1234, 5678, 90))
    print(modExp(1234, 5678, 90))
    print(math.pow(1234, 56) % 90)
