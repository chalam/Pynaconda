import itertools
from collections import deque


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)
a = [40, 30, 50, 46, 39, 44]
print(list(moving_average(a)))

dq = deque(a)
print(dq)
dq.rotate(3)    # rotate right
print(dq)
dq.rotate(-2)   # rotate left
print(dq)
dq.reverse()
print(dq)


def delete_nth(dq, n):
    print(dq)
    dq.rotate(-n)
    print(dq)
    print(dq.popleft())
    print(dq)
    dq.rotate(n)
    print(dq)
    return dq

delete_nth(dq, 3)
