def num_ways_inner(a, k):
    if k == 0:
        return 1
    s = len(a) - k
    # if a[s] == '0':
    #     return 0
    ways = num_ways_inner(a, k-1) # try one letters
    if k >= 2 and int(a[s:s+2]) <= 26:  # try two letters
        ways += num_ways_inner(a, k-2)
    return ways

def num_ways(a):
    return num_ways_inner(a, len(a))

def num_ways_inner_dp(a, k, memo):
    if k == 0:
        return 1
    s = len(a) - k
    # if a[s] == '0':
    #     return 0
    if memo[k] is not None:
        return memo[k]
    ways = num_ways_inner_dp(a, k-1, memo) # try one letters
    if k >= 2 and int(a[s:s+2]) <= 26:  # try two letters
        ways += num_ways_inner_dp(a, k-2, memo)
    memo[k] = ways
    return ways

def num_ways_dp(a):
    memo = [None] * (len(a) + 1)
    return num_ways_inner_dp(a, len(a), memo)

print(num_ways('12345'))
print(num_ways_dp('12345'))

print(num_ways('11111111'))
print(num_ways_dp('11111111'))