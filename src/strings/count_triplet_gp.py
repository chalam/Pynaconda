#!/bin/python3

import math
import os
import random
import re
import sys

def get_positions(arr, i):
    start_idx = 0
    pos=[]
    while start_idx < len(arr):
        try:
            p = arr.index(i, start_idx)
            pos.append(p)
            start_idx = p + 1
        except:
            break
    # print('pos of ',i,pos)
    return pos

# Complete the countTriplets function below.
def countTriplets(arr, r):
    max_n = max(arr)
    gp_r = []
    n = 0
    while r ** n <= max_n:
        gp_r.append(r ** n)
        n += 1
    # print(gp_r)
    total=[]
    for s in range(len(gp_r)-2):
        i, j, k = gp_r[s], gp_r[s+1], gp_r[s+2]
        # print(i, j, k)
        i_pos = get_positions(arr, i)
        j_pos = get_positions(arr, j)
        k_pos = get_positions(arr, k)
        for ii in i_pos:
            for jj in j_pos:
                for kk in k_pos:
                    # print(ii, jj, kk)
                    total.append((ii, jj, kk))
    # print('total', total)
    return len(total)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # nr = input().rstrip().split()
    #
    # n = int(nr[0])
    #
    # r = int(nr[1])
    #
    # arr = list(map(int, input().rstrip().split()))
    #
    # ans = countTriplets(arr, r)
    #
    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()

    assert countTriplets([1, 3, 9, 9, 27, 81], 3) == 6
    assert countTriplets([1, 5, 5, 25 ,125], 5) == 4
