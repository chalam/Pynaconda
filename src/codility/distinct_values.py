def distinct(A):
    A.sort()
    dist = []
    n = len(A)
    for i in range(1, n):
        if A[i] != A[i-1]:
            dist.append(A[i-1])
    return dist


if __name__ == '__main__':
    assert distinct([1,2,3,3,4,2,1,5]) == [4, 5]