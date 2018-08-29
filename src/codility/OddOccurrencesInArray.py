import pprint as pp
import numpy as np

def odd_array(A):
    N = len(A)
    if N % 2 == 0:
        return A

    seen = {}
    for i, a in enumerate(A):
        print(i, a)
        if a in seen:
            j = seen.pop(a)
            print('%d at %d matches with %d' % (a, j, i))
        else:
            seen[a] = i
    if len(seen) > 0:
        print(seen)
    return seen.popitem()[0]


if __name__ == '__main__':
    pp.pprint('%s : %s' % ([9,3,9,3,9,7,9], odd_array([9,3,9,3,9,7,9])))
    #
    # A = np.random.randint(-1000, 1000, 10).tolist()
    # K = np.random.randint(1, 10, 1)[0]
    # pp.pprint('%s >> %s == %s' % (A, K, cyclic_rotate(A, K)), width=1000)
