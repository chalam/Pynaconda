# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
# Input : X = "GeeksforGeeks", y = "GeeksQuiz"
# Output : 5
# The longest common substring is "Geeks" and is of
# length 5.
import math


def lcsubstr(x, y):
    m = len(x) + 1
    n = len(y) + 1
    lcs = [[0 for _ in range(n)] for _ in range(m)]
    result = -math.inf
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
                result = max(result, lcs[i][j]) # new max
    print(lcs)
    return result


assert lcsubstr('GeeksforGeeks', 'GeeksQuiz') == 5 # Geeks
assert lcsubstr('abcdxyz', 'xyzabcd') == 4 # abcd
assert lcsubstr('zxabcdezy', 'yzabcdezx') == 6 # abcdez