import unittest
import tasks
import numpy as np


class CheckMatrixTestCase(unittest.TestCase):
    def test_1t(self):
        a = np.array([[1, -12, 0],
                      [4, 6, 20],
                      [-1, 10, -1]])
        tasks.step_right(a)
        expected = np.array([[0, -12, 0],
                             [0, 0, 0],
                             [-1, 0, -1]])
        self.assertEqual(expected.all(), a.all())

    def test_1f(self):
        a = np.array([[1, -12, 0],
                      [4, 6, 1],
                      [-1, 10, 1]])
        tasks.step_right(a)
        expected = np.array([[1, -12, 0],
                             [4, 6, 1],
                             [-1, 10, 1]])
        self.assertEqual(expected.all(), a.all())

    def test_2t(self):
        a = np.array([[1, 1, -1],
                      [1, 20, -1],
                      [-1, 1, 1]])
        tasks.step_right(a)
        expected = np.array([[0, 0, -1],
                             [0, 0, -1],
                             [-1, 0, 0]])
        self.assertEqual(expected.all(), a.all())

    def test_2f(self):
        a = np.array([[1, 1, -1],
                      [1, 20, 1],
                      [-1, 1, 1]])
        tasks.step_right(a)
        expected = np.array([[1, 1, -1],
                             [1, 20, 1],
                             [-1, 1, 1]])
        self.assertEqual(expected.all(), a.all())

    def test_3(self):
        a = np.array([[1, 1, -1],
                      [1, 20, 0],
                      [-1, 1, 1]])
        tasks.step_right(a)
        expected = np.array([[0, 0, -1],
                             [0, 0, 20],
                             [-1, 0, 0]])
        self.assertEqual(expected.all(), a.all())

    def test_3(self):
        a = np.array([[1, 1, -1],
                      [1, 20, -2],
                      [-1, 1, 1]])
        tasks.step_right(a)
        expected = np.array([[1, 1, -1],
                             [1, 20, 21],
                             [-1, 1, 1]])
        self.assertEqual(expected.all(), a.all())

    def test_2_1(self):
        a = np.array([[1, 1, -1],
                      [1, 20, 21],
                      [-1, 1, 1]])
        res = tasks.can_not_step_right(a)
        expected = False
        self.assertEqual(expected, res)

    def test_2_2(self):
        a = np.array([[1, 1, -1],
                      [1, 20, 18],
                      [-1, 1, 1]])
        res = tasks.can_not_step_right(a)
        expected = False
        self.assertEqual(expected, res)

    def test_2_3(self):
        a = np.array([[1, 1, -1],
                      [1, 20, 19],
                      [-1, 1, 1]])
        res = tasks.can_not_step_right(a)
        expected = True
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
