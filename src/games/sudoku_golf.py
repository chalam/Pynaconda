# https://jakevdp.github.io/blog/2013/04/15/code-golf-in-python-sudoku/

# Write functions that, given an index 0 <= i < 81,
# return the indices of grid spaces in the same row,
# column, and box as entry i
def row_indices(i):
    start = i - i % 9
    return range(start, start + 9)


def col_indices(i):
    start = i % 9
    return range(start, start + 81, 9)


def box_indices(i):
    start = 27 * (i // 27) + 3 * ((i % 9) // 3)
    return [i for j in range(3) for i in range(start + 9 * j, start + 9 * j + 3)]


# compute and store the full set of connected indices for each i
connected = [(set.union(set(box_indices(i)),
                        set(row_indices(i)),
                        set(col_indices(i)))
              - set([i]))
             for i in range(81)]


# S(p) will recursively find solutions and "yield" them
def S(p):
    # First, find the number of empty squares and the number of
    # possible values within each square
    L = []
    for i in range(81):
        if p[i] == '0':
            vals = set('123456789') - set(p[n] for n in connected[i])
            if len(vals) == 0:
                return
            else:
                L.append((len(vals), i, vals))

    # if all squares are solved, then yield the current solution
    if len(L) == 0 and '0' not in p:
        yield p

    # otherwise, take the index with the smallest number of possibilities,
    # and recursively call S() for each possible value.
    else:
        N, i, vals = min(L)
        for val in vals:
            for s in S(p[:i] + val + p[i + 1:]):
                yield s




puz="027800061000030008910005420500016030000970200070000096700000080006027000030480007"
for s in S(puz):
    print(s)

puz = 81*'0'  # empty puzzle
print(next(S(puz)))

# def test(S):
#     # solve an empty puzzle
#     print(next(S(81*'0')))
#     print('')
#
#     # find all four solutions of puz
#     for s in S(puz):
#         print(s)
#
# test(S)