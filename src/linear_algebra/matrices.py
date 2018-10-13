A = [[1,2,3],
     [4,5,6]]

B = [[1,2],
     [3,4],
     [5,6]]


def shape(A):
    """n * k"""
    n_rows = len(A)
    n_cols = len(A[0]) if A else 0
    return [n_rows, n_cols]


def get_row(A, i):
    return A[i]


def get_col(A, j):
    """jth element of row A_i"""
    return [A_i[j] for A_i in A]


def make_matrix(n_rows, n_cols, entry_fn):
    return [[entry_fn(i, j)
            for j in range(n_cols)]
            for i in range(n_rows)]


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


def identity_matrix(n_rows, n_cols):
    return make_matrix(n_rows, n_cols, is_diagonal)

