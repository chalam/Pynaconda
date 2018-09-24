from src.dynamic_programming.memoize_decorator import memoize
# https://planetmath.org/listoffibonaccinumbers

def fib_memo(n, cached):
    """top down"""
    if n in cached:
        return cached[n]

    ret = fib_memo(n - 2, cached) + fib_memo(n - 1, cached)
    cached[n] = ret
    return ret

cached = {0: 0, 1: 1}
fib_n = fib_memo(50, cached)
assert fib_n == 12586269025
cached = {0: 0, 1: 1}
assert fib_memo(100, cached) == 354224848179261915075

@memoize
def fib_memo2(n):
    if n <= 2:
        return 1
    else:
        return fib_memo2(n - 1) + fib_memo2(n - 2)

assert fib_memo2(50) == 12586269025
assert fib_memo2(100) == 354224848179261915075

def fib_tabulation(n):
    """bottom up"""
    fib = {0: 0, 1: 1}
    for i in range(2, n + 1):
        fib[i] = fib[i - 2] + fib[i - 1]
    return fib[n]

assert fib_tabulation(50)== 12586269025
assert fib_tabulation(100) == 354224848179261915075

def get_fib_n(n):
    PHI = 1.61803398874989484820
    fib_n = (PHI ** n - (1 - PHI) ** n) / (5 ** 0.5)
    return fib_n

print(get_fib_n(50))
assert get_fib_n(50) == 12586269025.00002
