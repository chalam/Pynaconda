
class Memoize(object):
    """
    A decorator for caching function results.
    """

    def __init__(self, func):
        self._func = func
        self._cache = dict()

    def __call__(self, *args):
        if args not in self._cache:
            self._cache[args] = self._func(*args)
        return self._cache[args]


if __name__ == '__main__':
    # if invoking this script directly, time the `factorial` function
    # and its memoized variant, and print out the timings

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n* factorial(n - 1)


    @Memoize
    def factorial_with_memoize(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    import time

    N = 15
    REPETITIONS = 10000

    r1 = factorial(N)
    t0 = time.time()
    for x in range(REPETITIONS):
        factorial(N)
    t1 = time.time() - t0

    r2 = factorial_with_memoize(N)
    t0 = time.time()
    for x in range(REPETITIONS):
        factorial_with_memoize(N)
    t2 = time.time() - t0

    assert r1 == r2
    print("Times taken to compute factorial(%d)=%d:" % (N, r1))

    print("  * without memoization: %0.4f s" % t1)
    print("  * with memoization: %0.4f s" % t2)
