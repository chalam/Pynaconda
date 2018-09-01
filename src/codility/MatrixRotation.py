# #!/bin/python3
# import math
# import os
# import random
# import re
# import sys
# 
# # Complete the matrixRotation function below.
# def matrixRotation(matrix, r):
#     pass
# 
# def flat_list(listOfList):
#     return [item for sublist in listOfList for item in sublist]
# 
# def assign_ring(A, m, n):
#     mat = AA[0:n-1]
# 
# def rotate_ring(A, r):
#     return A[r:] + list(reversed(A[:r]))
# 
# def get_ring(matrix, m, n):
#     A = matrix[0][:n-1:]
#     A.extend([matrix[i][n-1] for i in range(m-1)])
#     A.extend(list(reversed(matrix[n - 1][1:n])))
#     A.extend([matrix[i][0] for i in range(m-1,0,-1)])
# 
# 
# if __name__ == '__main__':
#     m, n, r = map(int, input().rstrip().split())
# 
#     matrix = []
# 
#     for _ in range(m):
#         matrix.append(list(map(int, input().rstrip().split())))
# 
#     matrixRotation(matrix, r)


from copy import deepcopy
m, n, r = map(int, input().split())
matrix = []
for i in range(m):
    # matrix.append(map(int, input().rstrip().split()))
    matrix.append(list(map(int, input().rstrip().split())))
k = min(m, n) // 2
rows = []
for ii in range(k):
    row = []
    for i in range(ii, m - 1 - ii):
        row.append(matrix[i][ii])
    for i in range(ii, n - 1 - ii):
        row.append(matrix[m - 1 - ii][i])
    for i in range(m - 1 - ii, ii, -1):
        row.append(matrix[i][n - 1 - ii])
    for i in range(n - 1 - ii, ii, -1):
        row.append(matrix[ii][i])
    rows.append(row)

result = deepcopy(matrix)

for ii in range(k):
    row = rows[ii]
    shift = r % len(row)
    idx = -shift
    for i in range(ii, m - 1 - ii):
        result[i][ii] = row[idx]
        idx += 1
        idx %= len(row)
    for i in range(ii, n - 1 - ii):
        result[m - 1 - ii][i] = row[idx]
        idx += 1
        idx %= len(row)
    for i in range(m - 1 - ii, ii, -1):
        result[i][n - 1 - ii] = row[idx]
        idx += 1
        idx %= len(row)
    for i in range(n - 1 - ii, ii, -1):
        result[ii][i] = row[idx]
        idx += 1
        idx %= len(row)
for i in result:
    print( " ".join(map(str, i)))