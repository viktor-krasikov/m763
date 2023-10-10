import unittest
import tasks


class CheckMatrixTestCase(unittest.TestCase):
    def test_1(self):
        a = [[1, -12, 0],
             [4, 6, 20],
             [-1, 10, -1]]
        res = tasks.lavrentev_buldaev(a)
        expected = [[0, -12, 0],
                    [0, 0, 0],
                    [-1, 0, -1]]
        self.assertEqual(expected, res)

    def test_2(self):
        a = [[1, 1, -1],
             [1, 20, -1],
             [-1, 1, 1]]
        res = tasks.lavrentev_buldaev(a)
        expected = [[0, 0, -1],
                    [0, 0, -1],
                    [-1, 0, 0]]
        self.assertEqual(expected, res)

    def test_3(self):
        a = [[1, 1, -1],
             [1, 20, 0],
             [-1, 1, 1]]
        res = tasks.lavrentev_buldaev(a)
        expected = [[0, 0, -1],
                    [0, 0, 20],
                    [-1, 0, 0]]
        self.assertEqual(expected, res)

    def test_3(self):
        a = [[1, 1, -1],
             [1, 20, -2],
             [-1, 1, 1]]
        res = tasks.lavrentev_buldaev(a)
        expected = [[1, 1, -1],
                    [1, 20, 21],
                    [-1, 1, 1]]
        self.assertEqual(expected, res)

    def test_2_1(self):
        a = [[1, 1, -1],
             [1, 20, 19],
             [-1, 1, 1]]
        res = tasks.lavrentev_buldaev2(a)
        expected = True
        self.assertEqual(expected, res)

    def test_2_2(self):
        a = [[1, 1, -1],
             [1, 20, 18],
             [-1, 1, 1]]
        res = tasks.lavrentev_buldaev2(a)
        expected = False
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
