def solution(X, Y, D):
    # O(N)
    dist = X
    jump = 0
    while (dist <= Y):
        # print(dist)
        jump += 1
        dist += jump * D
    return jump

import math
def solution2(X, Y, D):
    # O(1)
    return math.ceil((Y-X)/float(D))

if __name__ == '__main__':
    assert solution(1, 5, 2) == 2
    assert solution(1, 5, 2) == 2