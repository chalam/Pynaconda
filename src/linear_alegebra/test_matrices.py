from unittest import TestCase
import matrices


class TestVector(TestCase):
    def test_shape(self):
        assert [2, 2] == matrices.shape([[1, 2], [3, 4]])

    def test_identity_matrix(self):
        assert [[1, 0], [0, 1]] == matrices.identity_matrix(2, 2)
        assert [[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]] == matrices.identity_matrix(4, 4)
