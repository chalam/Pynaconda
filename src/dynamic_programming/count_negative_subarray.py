def negative_subarray(A):
    sl = len(A)
    count = 0
    for i in range(sl):
        for j in range(i, sl):
            print(i, j, A[i:j + 1], count)
            if (sum(A[i:j + 1]) < 0):
                count += 1
    print(count)
    return count

assert negative_subarray([1, -2, 4, -5, 1]) == 9