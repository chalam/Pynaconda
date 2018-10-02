import itertools
import random
import sys


def distance(x, y, metric='euclid'):
    if metric == 'euclid':
        return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
    elif metric == 'manhattan':
        return (abs(x[0] - y[0]) + abs(x[1] - y[1]))

def near_neighbor_naive(points):
    min_dist = sys.maxsize
    for x, y in itertools.combinations(points, 2):
        dist = distance(x, y)
        print(x, y, dist)
        if dist < min_dist:
            print('min', x, y, dist)
            min_dist = dist
    return min_dist

def make_points(length: int = 5):
    lst1 = [random.randint(-10, 10) for i in range(length)]
    lst2 = [random.randint(-10, 10) for i in range(length)]
    return zip(lst1, lst2)

def prep_sort(points):
    a = list(dict.fromkeys(points))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    return ax, ay

# print(list(make_points(10)))
# points = [(-8, 7), (3, -2), (6, 2), (-7, 5), (-9, 2), (-4, 4), (3, -7), (-3, 9), (-1, -4)]
# print(near_neighbor_naive(points))
points = make_points(10)
ax, ay = prep_sort(points)
print(near_neighbor_naive(ax))
