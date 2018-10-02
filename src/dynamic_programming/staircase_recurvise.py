# given the njumps, find the nways to get to the top
def num_ways(n):
    if n <= 1:
        return 1
    return num_ways(n - 1) + num_ways(n - 2)

def num_ways_dp(n):
    dp = {0: 1, 1: 1}
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def num_ways_X(n):
    if n == 0:
        return 1
    return num_ways(n - 1) + num_ways(n - 3) + num_ways(n - 5)

def num_ways_dp_X(n, X):
    if n == 0:
        return 1
    total = 0
    for i in [1, 3, 5]:
        if n - i >= 0:
            total += num_ways_dp_X(n - i, X)
    return total

def num_ways_dp_bottom_up_X(n, X):
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for x in X:
            if i - x >= 0:
                total += dp[i - x]
        dp[i] = total
    return dp[n]

N = 4
print('N', N)
print(num_ways(N))
print(num_ways_dp(N))

N = 4
X = {1, 2}   # jumps
print('N', N, 'X', X)
print(num_ways_X(N))
print(num_ways_dp_X(N, X))
print(num_ways_dp_bottom_up_X(N, X))

N = 5
X = {1, 3, 5}   # jumps
print('N', N, 'X', X)
print(num_ways_X(N))
print(num_ways_dp_X(N, X))
print(num_ways_dp_bottom_up_X(N, X))
