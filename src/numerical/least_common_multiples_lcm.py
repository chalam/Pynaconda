# The least common multiple of 2 numbers, lcm(a,b), is the smallest number that is divisible by both a and b. The greatest common divisor of 2 numbers, gcd(a,b), is the largest number that divides both a and b.
# https://numericalrecipes.wordpress.com/2009/04/30/computing-the-greatest-common-divisor/
import time
from time import clock

from src.numerical.integer_factorization import factorAndSieve


def lcmBruteForce(a, b, verbose=False):
    t = clock()
    sieve = [0] * a * b
    a, b = max(a, b), min(a, b)
    for j in range(a - 1, a * b, a):
        sieve[j] += 1
    ret = 0
    for j in range(b - 1, a * b, b):
        if sieve[j] == 1:
            ret = j + 1
            break
    t = clock() - t
    if verbose:
        print("Calculated the lcm of", a, "and", b, "in", t, "sec.")
    return ret


def list_to_dict(seq):
    ret = dict()
    for j in seq:
        if j in ret:
            ret[j] += 1
        else:
            ret[j] = 1
    return ret


def gcd_factor(a, b, verbose=False):
    t = time.clock()
    aa = list_to_dict(factorAndSieve(a))
    bb = list_to_dict(factorAndSieve(b))
    rr = dict()
    for j in bb:
        if j in aa:
            rr[j] = min(aa[j], bb[j])
    ret = 1
    for j in rr:
        ret *= j ** rr[j]
    t = time.clock() - t
    if verbose:
        print("Calculated the gcd of", a, "and", b, "in", t, "sec.")
    return ret

def lcm_from_gcd(a, b, gcd):
    """lcm(a,b)·gcd(a,b) = a·b"""
    return a * b / gcd

if __name__ == '__main__':
    print(lcmBruteForce(4, 6))
    print(lcm_from_gcd(4, 6, gcd_factor(4, 6)))