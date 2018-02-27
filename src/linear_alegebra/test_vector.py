from unittest import TestCase
import vectors


class TestVector(TestCase):
    def test_vector_add(self):
        assert [4, 6] == vectors.vector_add([1, 2], [3, 4])

    def test_vector_subtract(self):
        assert [2, 2] == vectors.vector_subtract([3, 4], [1, 2])

    def test_vector_sum(self):
        assert [9, 12] == vectors.vector_sum([[1, 2], [3, 4], [5, 6]])
        assert [9, 12] == vectors.vector_sum1([[1, 2], [3, 4], [5, 6]])
        assert [9, 12] == vectors.vector_sum2([[1, 2], [3, 4], [5, 6]])

    def test_dot(self):
        assert 66 == vectors.dot([5, 12], [-6 , 8])
        assert 0 == vectors.dot([-12, 16], [12, 9])
        assert 122 == vectors.dot([9, 2, 7], [4, 8, 10])

    def test_cross(self):
        assert [5, 1, 11] == vectors.cross([2, 1, -1], [-3, 4, 1])
        assert [-5, -1, -11] == vectors.cross([-3, 4, 1],[2, 1, -1])
        assert [-3,  6, -3] == vectors.cross([1, 2, 3], [4, 5, 6])