def is_prime_naive(n):
    """sieve method """
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0:  # check if 'n' is a multiple of 2 or 3 (assumes you aren't checking 2 or 3 through this function)
        return False  # if it is, it's not prime
    sqrt = int(((n ** .5 + 1) // 1) - 1)  # efficient square root ceiling function ceil(sqrt(n))
    for x in range(5, sqrt, 2):  # check from 5 (next prime) to sqrt, but only every other number (the odds)
        if n % x == 0:  # if n is divisible by a number less than it (x)
            return False  # then it is not prime
    return True  # it has checked every number from [2, sqrt] and isn't divisible by any, so it is prime

# https://primes.utm.edu/lists/small/1000.txt
# assert is_prime_naive(1) == False
# assert is_prime_naive(1) == False
# assert is_prime_naive(3) == False
assert is_prime_naive(7697) == False
assert is_prime_naive(7699) == True
assert is_prime_naive(6449) == True


