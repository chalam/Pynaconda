from functools import partial

import math


def vector_add(v, w):
    """transform to v and then w """
    return [vi + wi for vi, wi in zip(v, w)]


def vector_subtract(v, w):
    return [vi - wi for vi, wi in zip(v, w)]


def vector_sum(vectors):
    """returns a vector whose ith comp is sum of ith comp of input vectors"""
    results = vectors[0]
    for vector in vectors[1:]:
        results = vector_add(results, vector)
    return results


def vector_sum1(vectors):
    return reduce(vector_add, vectors)


vector_sum2 = partial(reduce, vector_add)


def scalar_multiply(c, v):
    """ stretch or shrink """
    return [c * vi for vi in v]


def vector_mean(vectors):
    """compute vector whose ith element is mean of ith elements of input"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """scalar product a . b = ax * bx + ay * by"""
    return sum(vi * wi for vi, wi in zip(v, w))


def cross(a, b):
    """vector product scalar a x b = ax * bx + ay * by"""
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    """magnitude (or length)"""
    return math.sqrt(sum_of_squares(v))


def is_unit_vector(v):
    return magnitude(v) == 1


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v - w))


def distance(v, w):
    """sqrt of squared distance bw two vectors"""
    return math.sqrt(squared_distance(v - w))


def distance1(v, w):
    return magnitude(vector_subtract(v - w))
