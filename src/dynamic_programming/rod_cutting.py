import math


def cut_rod(p, n):
    """
    O(2^N) recursion
    :param p:
    :param n:
    :return:
    """
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

def cut_rod_memo(p, n):
    """
    top down in O(N^2) loop over recursive calls, but memoized
    :param p:
    :param n:
    :return:
    """
    r = [-math.inf] * (n + 1)

    def cut_rod_memo_aux(p, n, r):

        if r[n] >= 0:
            return r[n]
        if n == 0:
            return 0
        q = -math.inf
        for i in range(1, n+1):
            q = max(q, p[i] + cut_rod_memo_aux(p, n - i, r))
        r[n] = q
        return q

    return cut_rod_memo_aux(p, n, r)

def cut_rod_dp(p, n, c=1):
    """
    bottom up in O(N^2)
    :param p:
    :param n:
    :param c: cost/cut penalty
    :return:
    """
    r = [-math.inf] * (n + 1)
    s = r.copy()
    r[0] = 0
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            if q < p[i] + r[j - i] - c:
                q = p[i] + r[j - i] - c
                s[j] = i
        r[j] = q
    return r[n], s


def print_cut_rod(s, n):
    while n > 0:
        print(s[n])
        n -= s[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
nn = 4
max_rev = cut_rod(p, nn)
print('cut_rod', nn, max_rev)
assert max_rev == 10

nn = 9
max_rev = cut_rod_memo(p, nn)
print('cut_rod_memo', nn, max_rev)
assert max_rev == 25

max_rev, s = cut_rod_dp(p, nn)
print('cut_rod_dp', nn, max_rev, s)
assert max_rev == 23
print_cut_rod(s, nn)