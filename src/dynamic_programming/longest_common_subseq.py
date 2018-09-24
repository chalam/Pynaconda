# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# https://en.wikipedia.org/wiki/Longest_common_substring_problem
# https://www.youtube.com/watch?v=HgUOWB0StNE&list=PLqM7alHXFySGbXhWx7sBJEwY2DnhDjmxm&index=6
# https://www.hackerrank.com/challenges/common-child/problem

def lcs_len(x, y):
    """This recursive function returns length of longest common sequence of x and y."""

    if len(x) == 0 or len(y) == 0:
        return 0

    # xx = x[:-1]  # xx = sequence x without its last element
    # yy = y[:-1]

    if x[-1] == y[-1]:  # if last elements of x and y are equal
        return lcs_len(x[:-1], y[:-1]) + 1
    else:
        return max(lcs_len(x[:-1], y), #LCS without the last element
                   lcs_len(x, y[:-1]))

def make_matrix(m, n):
    return [[ 0 for _ in range(n)] for _ in range(m)]

# key:
# update on matching char
# carry over on filled neighbor on rest
def long_common_subseq(x, y):
    m = len(x) + 1
    n = len(y) + 1
    # if m > n:
    #     x, y = y, x
    #     m, n = n, m

    lcs = make_matrix(m, n)

    for i in range(1, m):
        for j in range(1, n):
            # print(x[i-1], y[j-1], x[i-1] == y[j-1])
            if x[i-1] == y[j-1]: # North West + 1, diagonally
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:              # max of West, North
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])
    print(lcs)
    return lcs[m-1][n-1], lcs

def reconstruct(i, j, lcs):
    if i == 0 or j == 0:
        return []
    elif x[i - 1] == y[j - 1]:
        return reconstruct(i - 1, j - 1, lcs) + [x[i - 1]]
    elif lcs[i - 1][j] > lcs[i][j - 1]:  # index out of bounds bug here: what if the first elements in the sequences aren't equal
        return reconstruct(i - 1, j, lcs)
    else:
        return reconstruct(i, j - 1, lcs)

x = 'AGCAT'
y = 'GAC'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 2

x = 'AGGTAB'
y = 'GXTXAYB'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 4

x = 'ABAB'
y = 'BABA'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 3

x = 'ABCD'
y = 'ABDC'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 3

x = 'SHINCHAN'
y = 'NOHARAAA'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 3

x = 'ABCDEF'
y = 'FBDAMN'
max_lcs, lcs = long_common_subseq(x, y)
print('max_lcs', max_lcs)
print(x, y, reconstruct(len(x), len(y), lcs))
assert max_lcs == 2

x = 'ABCDEF'
y = 'FBDAMN'
max_lcs = lcs_len(x, y)
print('lcs_len', max_lcs)
assert max_lcs == 2

x = 'abcdefg'
y = 'abxdfg'
max_lcs = lcs_len(x, y)
print('lcs_len', max_lcs)
assert max_lcs == 5