def fibo(max=10):
    a, b, i = 0, 1, 0
    while i < max:
        yield a
        a, b = b, a+b
        i += 1

def gen1():
    for i in [1, 2, 3]:
        yield i

def gen2():
    for i in 'abc':
        yield i

def gen():
    for val in gen1():
        yield val
    for val in gen2():
        yield val


if __name__ == '__main__':
    for i in fibo():
        print(i)
    for g in gen():
        print(g)