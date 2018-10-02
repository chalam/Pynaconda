#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    expected = []
    for i in range(0, n):
        expected.append(i + 1)
    total = 0
    for i in range(0, n):
        diff = abs(expected.index(q[i]) - i)
        # print(diff, q[i], expected[i])
        if diff > 2:
            print('Too chaotic')
            return
        if 0 < diff <= 2:
            total += diff
            temp = expected[i + diff]
            for j in range(i + diff, i, -1):
                expected[j] = expected[j - 1]
            expected[i] = temp
            # print('expecting', expected)
    print(total)

if __name__ == '__main__':
    # t = int(input())
    #
    # for t_itr in range(t):
    #     n = int(input())
    #
    #     q = list(map(int, input().rstrip().split()))
    #
    #     minimumBribes(q)

    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
    minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])
    minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])

# 2
# 8
# 5 1 2 3 7 8 6 4
# 8
# 1 2 5 3 7 8 6 4
