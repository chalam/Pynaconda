def solution(A):
    expected = (len(A)+2) * (len(A) + 1)/2
    for a in A:
        expected -= a
    return expected

def solution2(A):
    N = len(A) + 1
    expected = int((N * (N + 1)) / 2)
    for a in A:
        expected -= a
    return expected

if __name__ == '__main__':
    A = [1,3,5,2]
    assert solution(A) == 4
    assert solution2(A) == 4