import pprint as pp
import numpy as np

def cyclic_rotate(A, K):
    N = len(A)
    if K <= 0 or K == N or N == 0:
        return A
    if K > N:
        K = K % N

    # inefficient rotate once
    # AA = A
    # while K > 0:
    #     AA = AA[-1:] + AA[:-1]
    #     # print(AA)
    #     K -= 1
    # return AA

    return A[-K:] + A[:-K]


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    pp.pprint('%s : %s' % (A, cyclic_rotate(A, 3)))
    A = [0, 0, 0]
    pp.pprint('%s : %s' % (A, cyclic_rotate(A, 1)))
    A = [3, 8, 9, 7]
    pp.pprint('%s : %s' % (A, cyclic_rotate(A, 4)))
    A = [5, -1000]
    pp.pprint('%s : %s' % (A, cyclic_rotate(A, 1)))
    A = np.random.randint(-1000, 1000, 10).tolist()
    K = np.random.randint(1, 10, 1)[0]
    pp.pprint('%s >> %s == %s' % (A, K, cyclic_rotate(A, K)), width=1000)
