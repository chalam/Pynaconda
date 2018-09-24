# given values and weight, maximize the total value contraint by capacity weight W
# 0-1 propery is the item present or absent.. No fractional item
# https://en.wikipedia.org/wiki/Knapsack_problem
# https://www.youtube.com/watch?v=T4bY72lCQac&index=10&list=PLqM7alHXFySGbXhWx7sBJEwY2DnhDjmxm
# https://www.youtube.com/watch?v=EH6h7WA7sDw
def knapsack_recur(weights, W, values, n):
    """
    0-1 knapsack using optimal substructure recursion
    Time: O(n^2)
    :param weights: item wieghts
    :param W: maximum capacity
    :param values: item values
    :param n: number of items
    :return:
    """
    if n == 0 or W == 0:
        return 0

    # if weight of nth item is more that W, exclude it
    if weights[n - 1] > W:
        return knapsack_recur(weights, W, values, n-1)

    # the max  of two cases
    # 1. nth item included
    # 2. not included
    else:
        return max(values[n-1] + knapsack_recur(weights, W - weights[n-1], values, n-1), # nth item included
                   knapsack_recur(weights, W, values, n - 1)) # not included


def make_matrix(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]


# max of value of current item + memoized value due to the spare weight left over
def knapsack_dp(weights, W, values):
    """

    :param weights: weights per item
    :param W: Maximize to this weight
    :param values: values per item
    :return:
    """
    m = len(values) + 1
    n = W + 1
    dp = make_matrix(m, n)
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i-1] <= j:
                # print(weights[i - 1], values[i - 1], j)
                # max of add this item and value of whatever weight left or
                # excluding this item
                dp[i][j] = max(values[i - 1] + dp[i-1][j-weights[i - 1]],
                               dp[i-1][j]) # dont include this item, carry over from above
            else:
                dp[i][j] = dp[i-1][j] # carry from above
    print(dp)
    return dp[m-1][n-1], dp


# max of value of current item + memoized value due to the spare weight left over
def knapsack_unbounded(W, n, val, wt):
    # Returns the maximum value
    # with knapsack of W capacity
    # dp[i] is going to store maximum
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)]

    ans = 0

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    return dp[W]

def knapsack_show_items(res, K, val, wt):
    w = W
    n = len(values) + 1
    print('knapsack_show_items')
    for i in range(n, 0, -1):
        # print(i)
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
            # This item is included.
            print('index: %d, value: %d, weight: %d' % (i-1, values[i-1], wt[i - 1]))

            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]



values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
expected = 220
actual = knapsack_recur(weights, W, values, len(values))
print('expected', expected, 'actual', actual)
assert expected == actual

values = [5, 2, 4]
weights = [3, 2, 1]
W = 5
expected = 9
actual, dp = knapsack_dp(weights, W, values)
print('expected', expected, 'actual', actual)
assert expected == actual
knapsack_show_items(actual, dp, values, weights)

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
expected = 220
actual, dp = knapsack_dp(weights, W, values)
print('expected', expected, 'actual', actual)
assert expected == actual
knapsack_show_items(actual, dp, values, weights)

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
expected = 300
actual = knapsack_unbounded(W, len(values),values, weights)
print('expected', expected, 'actual', actual)
assert expected == actual

values = [1, 2]
weights = [1, 2]
W = 3
expected = 3
actual = knapsack_unbounded(W, len(values),values, weights)
print('expected', expected, 'actual', actual)
assert expected == actual
