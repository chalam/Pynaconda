def count_tiles(n, m, p):
    """
        calculating the number of distinct ways to fill an
        n× m grid using 1×p and p×1
    :param n: rows
    :param m: cols
    :param p: tile length
    :return:
    """
    dp = [0] * (n + 2)
    for i in range(1, n+1):
        if i > m:
            dp[i] = dp[i-1] + dp[i-m]
        elif i < m:
            dp[i] = 1
        else:
            dp[i] = 2
    return dp[n]


n = 2
m = 3
p = 3
assert count_tiles(n, m, p) == 1

n = 4
m = 4
p = 4
assert count_tiles(n, m, p) == 2

n = 7
m = 4
p = 4
assert count_tiles(n, m, p) == 5

n = 4
m = 7
p = 2
assert count_tiles(n, m, p) == 5