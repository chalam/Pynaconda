def solution(A):

    maxslice, ending = -float('inf'), None
    for value in A:
        ending = value if ending == None else max(value, ending + value)
        maxslice = max(ending, maxslice)
    return maxslice


if __name__ == '__main__':
    assert solution([3, 6, 64, -33, -60, 2, 94, -11, 12]) == 97