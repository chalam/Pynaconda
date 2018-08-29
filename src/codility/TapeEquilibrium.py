import pprint as pp
import numpy as np

def find_equiv(A):
    N = len(A)
    min_sum = float('inf')
    for i in range(N-1):
        curr = abs(sum(A[0:i+1]) - sum(A[i+1:]))
        # print(i, A[0:i+1], A[i+1:], curr)
        min_sum = min([min_sum, curr])
    return min_sum

def find_equiv2(A):
    total, minimum, left = sum(A), float('inf'), 0
    for a in A[:-1]:
        left += a
        minimum = min(abs(total - left - left), minimum)
    return minimum


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    pp.pprint('%s : %s' % (A, find_equiv(A)))
    assert find_equiv(A) == 7

    A = [3, 1, 2, 4, 3]
    pp.pprint('%s : %s' % (A, find_equiv(A)))
    assert find_equiv(A) == 1

    A = [-1000, 1000]
    pp.pprint('%s : %s' % (A, find_equiv(A)))
    assert find_equiv(A) == 2000

    A = [-1000, -1000]
    pp.pprint('%s : %s' % (A, find_equiv(A)))
    assert find_equiv(A) == 0

    A = [-1000, -1000, -1000]
    pp.pprint('%s : %s' % (A, find_equiv(A)))
    assert find_equiv(A) == 1000
    assert find_equiv(A) == find_equiv2(A)

    A = np.random.randint(-1000, 1000, 10000).tolist()
    pp.pprint('min_sum: %s' % (find_equiv(A)))
    assert find_equiv(A) == find_equiv2(A)

    A = np.random.randint(-100, 100, 100000).tolist()
    pp.pprint('min_sum2: %s' % (find_equiv2(A)))
    pp.pprint('min_sum: %s' % (find_equiv(A)))
    assert find_equiv(A) == find_equiv2(A)
