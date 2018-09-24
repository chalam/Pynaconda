# https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
# https://en.wikipedia.org/wiki/Subset_sum_problem

# Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.
import operator


def is_subset_sum_recur(a, n, sum):
    # O(2^N)
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    # exclude larger element
    if a[n-1] > sum:
        return is_subset_sum_recur(a, n - 1, sum)

    # included or excluded
    return is_subset_sum_recur(a, n - 1, sum - a[n-1]) or \
           is_subset_sum_recur(a, n - 1, sum)

def subset_sum_memo(a, n, sum):
    cache = {}

    def _subset_sum_memo(a, sum, i, cache):
        key = (sum, i)
        if key in cache:
            return cache(key)
        if sum == 0:
            return 1    # handles null-set {}
        elif sum < 0:
            return 0
        elif i < 0:
            return 0
        elif sum < a[i]:    # exclude larger than sum
            subsum = _subset_sum_memo(a, sum, i - 1, cache)
        else:
            subsum = (_subset_sum_memo(a, sum - a[i], i - 1, cache) + #include
                      _subset_sum_memo(a, sum, i - 1, cache))
        cache[key] = subsum
        return subsum

    return _subset_sum_memo(a, sum, n - 1, cache)

def is_subset_sum_dp(a, n, sum):
    # pseudo-polynomial O(n*sum)

    # // The value of subset[i][j] will be
    # // true if there is a subset of
    # // set[0..j-1] with sum equal to i
    dp = [[None for _ in range(n+1)] for _ in range(sum+1)]

    # If sum is 0, then answer is true
    for i in range(n+1):
        dp[0][i] = True

    # If sum is not 0 and set is empty, then False
    for i in range(1, sum+1):
        dp[i][0] = False

    # Fill the dp subset table in bottom-up
    for i in range(1, sum+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            if i >= a[j-1]:
                dp[i][j] = dp[i][j] or dp[i - a[j-1]][j-1]

    print(dp)
    return dp[sum][n]


def approx_with_accounting_and_duplicates(x_list,
                                s,      # target value
                                ):
    '''
    Modified from http://en.wikipedia.org/wiki/Subset_sum_problem#Polynomial_time_approximate_algorithm
         initialize a list S to contain one element 0.
         for each i from 1 to N do
           let T be a list consisting of xi + y, for all y in S
           let U be the union of T and S
           sort U
           make S empty
           let y be the smallest element of U
           add y to S
           for each element z of U in increasing order do
              //trim the list by eliminating numbers close to one another
              //and throw out elements greater than s
             if y + cs/N < z <= s, set y = z and add z to S
         if S contains a number between (1 - c)s and s, output yes, otherwise no
    '''
    c = .01              # fraction error (constant)
    N = len(x_list)      # number of values

    S = [(0, [])]
    for x in sorted(x_list):
        T = []
        for y, y_list in S:
            T.append((x + y, y_list + [x]))
        U = T + S
        U = sort_by_col(U, 0)
        y, y_list = U[0]
        S = [(y, y_list)]

        for z, z_list in U:
            lower_bound = (float(y) + c * float(s) / float(N))
            if lower_bound < z <= s:
                y = z
                S.append((z, z_list))

    return sort_by_col(S, 0)[-1]

def sort_by_col(table, col=0):
    '''
    http://www.saltycrane.com/blog/2007/12/how-to-sort-table-by-columns-in-python/
    '''
    return sorted(table, key=operator.itemgetter(col))

a = [3, 34, 4, 12, 5, 2]
assert is_subset_sum_recur(a, len(a), 9)
assert is_subset_sum_dp(a, len(a), 9)
assert subset_sum_memo(a, len(a), 9) == 2   # (3, 4, 2) and (4,5)
assert approx_with_accounting_and_duplicates(a, 9) == (9, [4, 5])

a = [4, 1, 10, 12, 5, 2]
assert is_subset_sum_recur(a, len(a), 9)
assert is_subset_sum_dp(a, len(a), 9)
assert subset_sum_memo(a, len(a), 9) == 1
assert approx_with_accounting_and_duplicates(a, 9) == (9, [4, 5])

a = [1, 8, 2, 5]
assert not is_subset_sum_recur(a, len(a), 4)
assert not is_subset_sum_dp(a, len(a), 4)
assert approx_with_accounting_and_duplicates(a, 9) == (9, [1, 8])
assert subset_sum_memo(a, len(a), 9) == 1
assert approx_with_accounting_and_duplicates(a, 4) == (3, [1, 2])


# zero is one subset of {}
assert is_subset_sum_recur(a, len(a), 0)
assert is_subset_sum_dp(a, len(a), 0)
assert subset_sum_memo(a, len(a), 0) == 1
assert approx_with_accounting_and_duplicates(a, 0) == (0, [])
