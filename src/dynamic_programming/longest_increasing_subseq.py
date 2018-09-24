# https://www2.cs.duke.edu/courses/spring17/cps130/Notes/dynamic.pdf
# https://www.youtube.com/watch?v=Ns4LCeeOFS4&index=5&list=PLqM7alHXFySGbXhWx7sBJEwY2DnhDjmxm
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence

# key:
# update on increasing sequnce
# carry over on rest
import math


def long_inc_subseq(a):
    # O(N^2)

    n = len(a)
    lis = [1] * n
    for i in range(1, n):       # 1 to n-1
        for j in range(0, i):   # 0 to i-1
            if a[i] > a[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
    return max(lis), lis

def long_inc_subseq_optimized(X):
    N = len(X)
    # more optimized using binary search O(N*logN)
    P = [0] * N # stores predecessor indexes
    M = [0] * (N + 1) # store index k of smallest
    L = 0 # holds the max_lis
    for i in range(N):
        # binary search for largest positive J <= L
        lo = 0
        hi = L
        while lo <= hi:
            mid = math.ceil((lo + hi) / 2)
            if X[mid] < X[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        # after search lo is 1 greater than the length of
        # longest prefix of X[i]
        newL = lo

        # The predecessor of X[i] is the last index of
        # subsequnce of lenght newL - 1
        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL) # we found a subseq longer than prev

    # reconstruct the long incr subseq
    S = [0] * L
    k = M[L]
    for i in range(L-1, 0, -1):
        S[i] = X[k]
        k = P[k]

    return L, S





# a = [11, 14, 13, 7, 8, 15]
# max_lis, lis = long_inc_subseq(a)
# print('max_lis', max_lis, 'lis', lis)
# assert max_lis == 3
#
# a = [10, 22, 9, 33, 21, 50, 41, 60]
# max_lis, lis = long_inc_subseq(a)
# print('max_lis', max_lis, 'lis', lis)
# assert max_lis == 5
#
# a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# max_lis, lis = long_inc_subseq(a)
# print('max_lis', max_lis, 'lis', lis)
# assert max_lis == 6

a = [10, 22, 9, 33, 21, 50, 41, 60]
max_lis, lis = long_inc_subseq_optimized(a)
print('max_lis', max_lis, 'lis', lis)
assert max_lis == 5