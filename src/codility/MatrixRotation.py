#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    pass

def flat_list(listOfList):
    return [item for sublist in listOfList for item in sublist]

def assign_ring(A, m, n):
    mat = AA[0:n-1]

def rotate_ring(A, r):
    return A[r:] + list(reversed(A[:r]))

def get_ring(matrix, m, n):
    A = matrix[0][:n-1:]
    A.extend([matrix[i][n-1] for i in range(m-1)])
    A.extend(list(reversed(matrix[n - 1][1:n])))
    A.extend([matrix[i][0] for i in range(m-1,0,-1)])


if __name__ == '__main__':
    m, n, r = map(int, input().rstrip().split())

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)