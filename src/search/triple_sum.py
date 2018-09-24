# https://www.hackerrank.com/challenges/triple-sum

from bisect import bisect


# find p, q, r such that p <= q >= r in a, b, c
def triplets(a, b, c):
    a, b, c = sorted(set(a)), sorted(set(b)), sorted(set(c))
    return sum([bisect(a, x) * bisect(c, x) for x in reversed(b)])


a = [1, 3, 5, 7]
b = [5, 7, 9]
c = [7, 9, 11, 13]
sum = triplets(a, b, c)
print(sum)

a = [3, 5, 7]
b = [3, 6]
c = [4, 6, 9]
sum = triplets(a, b, c)
print(sum)
