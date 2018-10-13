# https://www.youtube.com/watch?v=XKu_SEDAykw
# does array has any pair that sum to s?

def has_pair_sum_brute(a, s):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # print(a[i], a[j])
            if (a[i] + a[j]) == s:
                return True
    return False


def has_pair_sum(a, s):
    """
    O(N)
    :param a:
    :param s:
    :return:
    """
    complements = set()
    for val in a:
        if val in complements:
            return True
        complements.add(s - val)
    return False


a = [1, 5, 7, -1, 5]
s = 6
assert has_pair_sum(a, s)
assert has_pair_sum_brute(a, s)

a = [1, 2, 3, 9]
s = 8
assert not has_pair_sum(a, s)
assert not has_pair_sum_brute(a, s)

a = [1, 2, 4, 4]
s = 8
assert has_pair_sum(a, s)
assert has_pair_sum_brute(a, s)

a = [2, 3, 4, -3, 0, 4, -1, 5]
s = 8
assert has_pair_sum(a, s)
assert has_pair_sum_brute(a, s)

a = [4, 5, -1]
s = 10
assert not has_pair_sum(a, s)
assert not has_pair_sum_brute(a, s)
a = [2, 3, 3]
s = 6
assert has_pair_sum(a, s)
assert has_pair_sum_brute(a, s)

a = [2, 3, 3]
s = 6
assert has_pair_sum(a, s)
assert has_pair_sum_brute(a, s)