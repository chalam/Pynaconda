import numpy as np
import random

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def make_2d_matrix_np(m, n):
    return np.zeros(m * n, dtype=int).reshape(m, n).tolist()

def make_2d_matrix(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]

def make_arrary(length=10, N=100, negatives=False):
    if negatives:
        return [random.randint(N * -1, N) for i in range(length)]
    else:
        return [random.randint(0, N) for i in range(length)]
