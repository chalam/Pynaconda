# S is set of nodes not yet visited
# dist(i, 1) = cost of i to 1
# If size of S is 2, then S must be {1, i},
#  C(S, i) = dist(1, i)
# Else if size of S is greater than 2.
#  C(S, i) = min { C(S-{i}, j) + dis(j, i)} where j belongs to S, j != i and j != 1.

# Naive is O(N!) since we have (N-1) possibilities
# DP= O(n^2 * 2^n)