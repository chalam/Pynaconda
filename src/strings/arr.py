
if __name__ == '__main__':
    pos = []
    a = [1, 5, 5, 25]
    start_idx = 0

    while start_idx < len(a):
        try:
            p = a.index(25, start_idx)
            pos.append(p)
            start_idx = p + 1
        except:
            break
    print(pos)
    for i in range(1):
        for j in range(2):
            for k in range(1):
                print(i,j,k)
