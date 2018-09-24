# https://www.hackerrank.com/challenges/max-array-sum/

"""
max @ position 0: value @ 0
max @ position 1: either:
    value @ 0
    value @ 1

from that point forward, the max of the next position is either:
    the current value at that position
    the max value found so far
    the max value from 2 positions back plus the current value

keep track of the max at each position until you get to the last position of the array
"""
def maxSubsetSum(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[1], dp[0])
    for i in range(2, len(arr)):
        dp[i] = max(arr[i],
                    dp[i-1],
                    arr[i] + dp[i-2])
    print(dp, dp[-1])
    return dp[-1]


assert maxSubsetSum([3, 7, 4, 6, 5]) == 13
assert maxSubsetSum([2, 1, 5, 8, 4]) == 11
assert maxSubsetSum([3, 5, -7, 8, 10]) == 15