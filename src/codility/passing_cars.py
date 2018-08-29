
def prefix_sums(A):
    n = len(A)
    p = [0] * (n+1)
    for i in range(1, n+1):
        p[i] = p[i-1] + A[i-1]
    return p

def count_total(p, x, y):
    return p[y] - p[x]

def passing_cars(A):
    n = len(A)
    pref = prefix_sums(A)
    print(pref)
    count = 0
    for i in range(n):
        if A[i] == 0:
            print(i)
            left_pos = i
            right_pos = n
            count += count_total(pref, left_pos, right_pos)

    if count > 1000000000:
        return -1
    return count

def passing_cars2(A):
    right,total = 0,0
    for left in A:
        right, total = (right + 1, total) if not left else (right, total + right)
    return total if total < 1000000000 else -1

if __name__ == '__main__':
    A = [0, 1, 0, 1, 1]
    count = passing_cars(A)
    assert count == 5
    assert passing_cars2(A) == 5


    # import numpy as np
    # np.random.seed()
    # A = np.random.randint(0, 2, 10).tolist()
    A = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    count = passing_cars(A)
    assert count == 17
    assert passing_cars2(A) == 17