# https://www.hackerrank.com/challenges/matrix-tracing/problem

# mod = 10**9 + 7
#
#
# def getfactmod(b):
#     val = 1
#     for i in range(1, b):
#         val = ((val % mod) * ((i + 1) % mod)) % mod
#     return val
#
#
# def getpowermod(a, b):
#     if b == 0:
#         return 1
#     if b == 1:
#         return a
#     temp = getpowermod(a, b / 2)
#     if b % 2 == 0:
#         return ((temp % mod) ** 2) % mod
#     else:
#         return (a * ((temp % mod) ** 2)) % mod
#
#
# def inversemod(a):
#     return getpowermod(a, mod - 2)
#
# T = int(input())
# assert 1 <= T <= 10**3
# for _ in range(T):
#     a, b = map(int, input().split())
#     assert 1 <= a <= 10**6
#     assert 1 <= b <= 10 ** 6
#     denominator = 1
#     numerator = 1
#     for i in range(1, a + b - 1):
#         numerator = ((numerator % mod) * (i % mod)) % mod
#     for i in range(1, a):
#         denominator = ((denominator % mod) * (i % mod)) % mod
#     for i in range(1, b):
#         denominator = ((denominator % mod) * (i % mod)) % mod
#     answer = ((numerator % mod) * (inversemod(denominator) % mod)) % mod
#     print(answer)

c = 10 ** 9 + 7


def fact(n):
    result = 1
    while n >= 2:
        result = ((result) * (n % c)) % c
        n -= 1
    return result


def fastEXP(base, exp, modulus):
    base %= modulus
    result = 1

    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp >>= 1

    return result


def combinations(x, y):
    amodc = fact(x + y - 2)
    bmodc = fact(x - 1) * fact(y - 1)
    return ((amodc % c) * (fastEXP(bmodc, (c - 2), c))) % c


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(combinations(y, x))

# print(combinations(2, 3))
# assert combinations(2, 3) == 3
# print(combinations(7, 5))
# assert combinations(7, 5) == 210
