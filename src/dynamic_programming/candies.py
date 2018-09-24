#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    dp = [1] * n
    for i in range(1, n):  # (int i = 1 ; i < n  ;i++){ //forward track
        print(i, arr[i-1], arr[i])
        if (arr[i] > arr[i - 1]):
            dp[i] = dp[i] + dp[i - 1]
    print(dp)
    for i in range(n - 2, 0, -1):  # (int i = n-2 ; i >= 0 ; i--){ // back track
        print(i, arr[i], arr[i+1])
        if (arr[i] > arr[i + 1] and dp[i] <= dp[i + 1]):
            dp[i] = dp[i + 1] + 1
    print(dp)
    return sum(dp)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())

    # arr = []

    # for _ in range(n):
    #     arr_item = int(input())
    #     arr.append(arr_item)

    arr = [2,4,2,6,1,7,8,9,2,1]
    n = 10
    result = candies(n, arr)
    print('result', result)
    assert result == 19

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
