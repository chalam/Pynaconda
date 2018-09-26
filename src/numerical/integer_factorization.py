# https://en.wikipedia.org/wiki/Integer_factorization
# https://numericalrecipes.wordpress.com/2009/04/09/naive-integer-factorization/

from time import clock
from src.numerical.find_primes import primeListSofE


def factor(n, verbose=True):
    """
    Returns all prime factors of n, using trial division by prime
    numbers only. Returns a list of (possibly repeating) prime factors
    """
    t = clock()
    ret = []
    nn = n
    maxFactor = int(n ** 0.5)
    primes = primeListSofE(maxFactor, verbose)
    for p in primes:
        while nn % p == 0:
            nn //= p
            ret += [p]
        if nn == 1:
            break
    if nn != 1:
        ret += [nn]
    t = clock() - t
    if verbose:
        print("Calculated factors of", n, "in", t, "sec.")
    return ret

def factorAndSieve(n, verbose = True) :
    """
    Returns all prime factors of n, using trial division while sieving
    for primes. Returns a list of (possibly repeating) prime factors
    general number field sieve (GNFS) algorithm,
    """
    t = clock()
    ret =[]
    nn = n
    while nn % 2 == 0 : # remove 2's first, as 2 is not in sieve
        nn //= 2
        ret += [2]
    maxFactor = int(nn**0.5)
    maxI = (maxFactor-3) // 2
    maxP = int(maxFactor**0.5)
    sieve = [True for j in range(maxI+1)]
    i = 0
    for p in range(3, maxP+1,2) : # we then sieve as far as needed
        if p > maxP :
            break
        i = (p-3) // 2
        if sieve[i] :
            while nn % p == 0 :
                nn //= p
                ret += [p]
                maxFactor = int(nn**0.5)
                maxI = (maxFactor-3) // 2
                maxP = int(maxFactor**0.5)
            if nn == 1 :
                break
            else :
                i2 = (p*p - 3) // 2
                for k in range(i2, maxI+1, p) :
                    sieve[k] = False
    index = i
    for i in range(index, maxI+1) : # and inspect the rest of the sieve
        if i > maxI :
            break
        if sieve[i] :
            p = 2*i + 3
            while nn % p == 0 :
                nn //= p
                ret += [p]
                maxFactor = int(nn**0.5)
                maxI = (maxFactor-3) // 2
                maxP = int(maxFactor**0.5)
            if nn == 1 :
                break
    if nn != 1 :
        ret += [nn]
    t = clock() - t
    if verbose :
        print("Calculated factors of",n,"in",t,"sec.")
        print("Stopped trial division at",2*i+3,"instead of",int(n**0.5))
    return ret

if __name__ == '__main__':
    # print(factor(10**15+37))    # 11 sec
    # print(factor(2**55))  # 72 sec
    print(factorAndSieve(10 ** 15 + 37))  # 4.7 sec
    print(factorAndSieve(2 ** 55))  # 4.6 sec

    # https://en.wikipedia.org/wiki/Integer_factorization
    print(factorAndSieve(864))  # 4.7 sec
