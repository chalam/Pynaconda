import numpy as np

def prefix_sums(A):
    n = len(A)
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + A[i - 1]
    return p

def count_total(p, x, y):
    return p[y+1] - p[x]

def mushroom_picker(A, k, m): #k-th spot, m - moves
    # O(n+m)
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    # make p moves in one direction, we can calculate the maximal opposite location of the mushroom picker
    for p in range(min(k, m) + 1): # 0 to m
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p)) # need to walk back 2*p
        print('1', left_pos, right_pos)
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in range(min(m + 1, n - k)):
        left_pos = k + p
        right_pos = max(0, min(k, k - (m - 2 * p)))
        print('2', left_pos, right_pos)
        result = max(result, count_total(pref, left_pos, right_pos))
    return result

if __name__ == '__main__':
    A = [1,2,3,4,5]
    print(A)

    p=prefix_sums(A)
    print(p)

    # sum b/w 3,4
    assert count_total(p, 3, 4) == 9
    assert count_total(p, 1, 3) == 9

    A = [2, 3, 7, 5, 1, 3, 9]
    p = prefix_sums(A)
    print(A, p)
    assert count_total(p, 2, 6) == 25

    # np.random.seed(12345)
    # A = np.random.randint(1, 10, 10).tolist()
    A = [7, 5, 2, 2, 6, 3, 5, 1, 2, 8]
    p = prefix_sums(A)
    print(A, p)
    print('max mushrooms', mushroom_picker(A, 5, 4))

