def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


def swap_check_slow(A, B, m):
    n = len(A)
    sum_A = sum(A)
    sum_B = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_A += change
            sum_B -= change
            if sum_A == sum_B:
                return True
            sum_A -= change
            sum_B += change
    return False

def swap_check_fast(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d % 2 == 1:
        return False
    d //= 2
    count = counting(A, m)
    for i in range(n):
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            return True
    return False


if __name__ == '__main__':
    A = [1,2,3,2,4,1,4,4,1,2]
    count = counting(A, 4)
    print(count)

    A = [2, 1, 3, 4]
    B = [1, 2, 3, 9]
    print('same: ', swap_check_slow(A, B, 4))
    print('same: ', swap_check_fast(A, B, 4))

    A = [2, 1, 3, 4]
    B = [1, 2, 4, 3]
    print('same: ', swap_check_slow(A, B, 4))
    print('same: ', swap_check_fast(A, B, 4))