from math import factorial


def combination(n, r):
    return int((factorial(n)) / ((factorial(r)) * factorial(n - r)))


def pascals_triangle(rows):
    result = []
    for count in range(rows + 1):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result

def pascals_triangle_nth_row(row):
    res = [1]
    y = [0]
    for i in range(row):
        # print(res)
        # zip two stream of previous row with zero prefix and zero suffix
        res = [l + r for l, r in zip(res + y, y + res)]

    # print(res[col])
    return res


if __name__ == '__main__':
    n = 5
    rows = pascals_triangle(n)
    for i in range(n + 1):
        print("   " * (n - i), end=" ", sep=" ")
        for j in range(i + 1):
            print('{0:6}'.format(rows[i][j]), end=" ", sep=" ")
        print()

    res = pascals_triangle_nth_row(n)
    assert res == rows[-1]
