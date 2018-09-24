
def group_alpha_num(s):
    """
        we cannot use extra nums and alpha list to separate
    :param a:
    :return:
    """
    first_num_idx = -1
    last_num_idx = -1
    # last_alpha_idx = -1
    # first_alpha_idx = -1
    a = [i for i in s] # limitation of py with str immutable
    for i in range(len(a)):
        print(i, a[i], a)
        if str.isdigit(a[i]):
            if first_num_idx < 0:
                first_num_idx = i
                last_num_idx = i
            else:
                if last_num_idx + 1 != i:
                    for j in range(i, last_num_idx + 1, -1):
                        a[j], a[j-1] = a[j-1], a[j] # str immutable
                last_num_idx += 1
        # if str.isalpha(a[i]):
        #     if first_alpha_idx < 0:
        #         first_alpha_idx = i
        #         last_alpha_idx = i
        #     else:
        #         if last_alpha_idx + 1 != i:
        #             for j in range(i, last_alpha_idx + 1, -1):
        #                 a[j], a[j - 1] = a[j - 1], a[j]
        #         last_alpha_idx += 1
        print(i, a[i], a)
    return ''.join(a)

def group_alpha_num(s):
    """
        we cannot use extra nums and alpha list to separate
    :param a:
    :return:
    """
    first_num_idx = -1
    last_num_idx = -1
    # last_alpha_idx = -1
    # first_alpha_idx = -1
    a = [i for i in s] # limitation of py with str immutable
    for i in range(len(a)):
        print(i, a[i], a)
        if str.isdigit(a[i]):
            if first_num_idx < 0:
                first_num_idx = i
                last_num_idx = i
            else:
                if last_num_idx + 1 != i:
                    for j in range(i, last_num_idx + 1, -1):
                        a[j], a[j-1] = a[j-1], a[j] # str immutable
                last_num_idx += 1
        print(i, a[i], a)
    return ''.join(a)

if __name__ == '__main__':
    s = '12gh45fd3'
    r = group_alpha_num(s)
    print(s, r)
    assert r == '12453ghfd'
