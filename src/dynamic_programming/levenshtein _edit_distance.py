# https://en.wikipedia.org/wiki/Levenshtein_distance

import numpy as np

def make_matrix(m, n):
    return np.zeros(m * n, dtype=int).reshape(m, n).tolist()


# key:
# matched so no cost changes
# unmatched minimum of all possibilities filled neighbor
def edit_dist(x, y):
    m = len(x) + 1
    n = len(y) + 1
    # if m > n:
    #     x, y = y, x
    #     m, n = n, m

    lev = make_matrix(m, n)

    for i in range(m):
        for j in range(n):
            # first string is empty, only option is to insert all char to second string
            if i == 0:
                lev[i][j] = j
            # second string is empty, only option is to insert all char to first string
            elif j == 0:
                lev[i][j] = i
            # if last char are same, ignore since no cost to change
            elif x[i-1] == y[j-1]:
                lev[i][j] = lev[i-1][j-1]
            # all possibility with min of insert, update, delete
            else:
                lev[i][j] = 1 + min(lev[i - 1][j],  # delete
                                lev[i][j - 1],      # insert
                                lev[i - 1][j - 1])  # replace
    print(lev)
    return lev[m - 1][n - 1]

x = 'MARCH'
y = 'CART'
lev = edit_dist(x, y)
print('levenshtein_edit_dist', lev)
assert lev == 3

x = 'kitten'
y = 'sitting'
lev = edit_dist(x, y)
print('levenshtein_edit_dist', lev)
assert lev == 3

x = 'saturday'
y = 'sunday'
lev = edit_dist(x, y)
print('levenshtein_edit_dist', lev)
assert lev == 3