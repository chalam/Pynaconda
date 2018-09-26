# https://numericalrecipes.wordpress.com/2009/03/16/prime-numbers-2-the-sieve-of-erathostenes/
# https://numericalrecipes.wordpress.com/2009/03/24/prime-numbers-3-wheel-factorization/

from math import sqrt
from time import time
from src.numerical.modular_multiplicative_inverse import modInvEuclid

def primeList1(n, verbose=True):
    # O(N^2)
    t = time()
    ret = []
    for j in range(2, n + 1):
        jIsPrime = True
        for k in range(2, j):
            if j % k == 0:
                jIsPrime = False
                break
        if jIsPrime:
            ret += [j]
    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")

    return ret


def primeList2(n, verbose=True):
    # O(sqrt(N))
    t = time()
    ret = []
    for j in range(2, n + 1):
        jIsPrime = True
        kMax = int(sqrt(j))
        for k in range(2, kMax + 1):
            if j % k == 0:
                jIsPrime = False
                break
        if jIsPrime:
            ret += [j]
    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")

    return ret


def primeList3(n, verbose=True):
    # O(sqrt(N)) + trial division to skip multiples of primes
    t = time()
    ret = []
    for j in range(2, n + 1):
        jIsPrime = True
        kMax = sqrt(j)
        for k in ret:  # use the primes already discovered
            if k > kMax:
                break
            if j % k == 0:
                jIsPrime = False
                break
        if jIsPrime:
            ret += [j]

    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")

    return ret


def primeListSofE(n, verbose=True):
    """
    Sieve of Erathostenes
    No costly trial division, use step range to skip multiples of primes
    O(n.log(n))(log(log(n)))
    :param n:
    :param verbose:
    :return:
    """
    t = time()
    sieve = [True for j in range(2, n + 1)]
    for j in range(2, int(sqrt(n)) + 1):
        i = j - 2
        if sieve[i]:
            for k in range(j * j, n + 1, j):
                sieve[k - 2] = False

    ret = [j for j in range(2, n + 1) if sieve[j - 2]]

    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")

    return ret


def primeListSofE_opt(n, verbose=True):
    """
    Returns a list of prime numbers smaller than or equal to n,
    using an optimized sieve of Erathostenes algorithm.
    Space optimized
    """
    t = time()
    maxI = (n - 3) // 2
    maxP = int(sqrt(n))
    sieve = [True for j in range(maxI + 1)]
    for p in range(3, maxP + 1, 2):
        i = (p - 3) // 2
        if sieve[i]:
            i2 = (p * p - 3) // 2
            for k in range(i2, maxI + 1, p):
                sieve[k] = False
    ret = [2] + [2 * j + 3 for j in range(len(sieve)) if sieve[j]]
    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")
    return ret


def primeListWF(n, m, verbose=True):
    """Returns a list of prime numbers smaller than or equal to n,
    using wheel factorization, with a wheel size of the product of
    all primes smaller than or equal to m
    https://numericalrecipes.wordpress.com/2009/03/24/prime-numbers-3-wheel-factorization/
    """
    t = time()
    # We use the standard sieve of Eratosthenes first...
    primes = primeListSofE(m)
    M = 1
    for p in primes:
        M *= p
    if verbose:
        print("Size of factorization wheel is", M)
    # We now sieve out all multiples of these primes,including
    # the primes themselves, to get the k[i]
    sieve = [True] * M
    for p in primes:
        sieve[p - 1] = False
        for j in range(p * p, M + 1, p):
            sieve[j - 1] = False
    k = [j + 1 for j in range(M) if sieve[j]]
    if verbose:
        print("Memory use is only", len(k), "/", M, "=", len(k) / M)
    N = n
    if N % M:
        N += M
    N //= M
    maxP = int(sqrt(M * N))
    if verbose:
        print("Primes will be calculated up to", M * N, "not", n)

    sieve = [[True] * N for j in range(len(k))]
    sieve[0][0] = False  # Take care of the non primality of 1
    for row in range(N):
        baseVal = M * row
        for subset in range(len(k)):
            if sieve[subset][row]:
                p = baseVal + k[subset]
                primes += [p]
                if p > maxP:
                    continue
                # Sieve all multiples of p...
                invMp = modInvEuclid(M, p)
                for i in range(len(k)):
                    mi = invMp * (-k[i] % p)
                    mi %= p
                    # ...starting at p**2
                    ji = (p * p - k[i] - M * mi)
                    if ji % (M * p):
                        ji += M * p
                    ji //= M * p
                    mi += ji * p

                    for r in range(mi, N, p):
                        sieve[i][r] = False
    if verbose:
        print("Calculated primes to", n, "in", time() - t, "sec.")

    return primes

if __name__ == '__main__':
    # print(primeList1(9973))
    print(primeList2(9973))
    print(primeList3(9973))
    print(primeListSofE(9973))
    print(primeListSofE_opt(9973))
    print(primeListWF(9973, 2)) # m = 2, 7, 11
