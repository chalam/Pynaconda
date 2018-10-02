# zig zag as in jpeg
# http://en.wikipedia.org/wiki/Image:JPEG_ZigZag.svg
import pprint

#  0  1  5  6 14
#  2  4  7 13 15
#  3  8 12 16 21
#  9 11 17 20 22
# 10 18 19 23 24

def zig_zag(m, n):
    i = j = k = 0
    a = [[None for j in range(n)] for i in range(m)]
    while k < m * n:
        # already in top row or right col
        if i == 0 or j == n - 1:
            print(i, j, k)
            a[i][j] = k
            k += 1
            if j+1 < n:     # step right
                j += 1
            elif j == n - 1:  # step down
                i += 1

        # diagonally down
        while j > 0 and i < m - 1:
            print(i, j, k)
            a[i][j] = k
            k += 1
            i += 1
            j -= 1

        # already in bottom row or left col
        if j == 0 or i == m - 1:
            print(i, j, k)
            a[i][j] = k
            k += 1
            if i + 1 < m:   # step down
                i += 1
            elif i == m - 1:  # step right
                j += 1

        # diagonally up
        while i > 0 and j < n - 1:
            print(i, j, k)
            a[i][j] = k
            k += 1
            i -= 1
            j += 1

    return a


m = 5   # rows
n = 8   # cols
# a = [[(i*n)+j for j in range(n)] for i in range(m)]
aa = zig_zag(m, n)
pprint.pprint(aa)

# http://rosettacode.org/wiki/Zig-zag_matrix#Groovy
def zig_zag_2(n):
    a = [[None for j in range(n)] for i in range(n)]
    i = j = 1
    for el in range(n * n):
        a[i - 1][j - 1] = el
        if (i + j) % 2 == 0:
            # even stripes
            if j < n:
                j += 1
            else:
                i += 2
            if i > 1:
                i -= 1
        else:
            # odd stripes
            if i < n:
                i += 1
            else:
                j += 2
            if j > 1:
                j -= 1
    return a

aa = zig_zag_2(m)
pprint.pprint(aa)



# http://paddy3118.blogspot.com/2008/08/zig-zag.html
def zigzag(n):
    indexorder = sorted(((x,y) for x in range(n) for y in range(n)),
        key = lambda p: (p[0]+p[1], -p[1] if (p[0]+p[1]) % 2 else p[1]) )
    return dict((index,n) for n,index in enumerate(indexorder))

def printzz(myarray):
    n = int(len(myarray)** 0.5 +0.5)
    for x in range(n):
        for y in range(n):
            print("%2i" % myarray[(x,y)],)
        print()

# printzz(zigzag(5))
