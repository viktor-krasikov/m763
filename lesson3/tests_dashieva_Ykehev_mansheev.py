import unittest
import tasks


class CheckMatrixTestCase(unittest.TestCase):
    def test_1(self):
        a = [[1, -12, 0],
             [4, 6, -8],
             [-1, 10, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, -12, 0],
                    [0, 0, -8],
                    [-1, 0, -1]]
        self.assertEqual(expected, res)

    def test_2(self):
        a = [[4, 2, -2],
             [-1, -2, -1],
             [12, 3, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, 0, -2],
                    [-1, -2, -1],
                    [0, 0, -1]]
        self.assertEqual(expected, res)

    def test_3(self):
        a = [[1, 2, 4, 29],
             [3, 4, 6, 1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, 0, 0, 0],
                    [0, 0, 0, 0]]
        self.assertEqual(expected, res)

    def test_4(self):
        a = [[1, 4, 0, 12],
             [-5, 8, 9, 0],
             [-6, 7, 0, 19]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, 3, 0, 11],
                    [-5, 7, 8, 0],
                    [-6, 6, 19, 18]]
        self.assertEqual(expected, res)

    def test_5(self):
        a = [[1, 4, 0, 12],
             [-5, -2, 30, 0],
             [-6, 4, 25, 19],
             [-7, 7, 0, 4],
             [-10, 7, 0, 14]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[1, 4, 0, 12],
                    [-5, 31, 30, 0],
                    [-6, 4, 25, 19],
                    [-7, 7, 0, 4],
                    [-10, 7, 0, 14]]
        self.assertEqual(expected, res)

    def test_6(self):
        a = [[-1, -1, -1],
             [-1, -1, -1],
             [-1, -1, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[-1, -1, -1],
                    [-1, -1, -1],
                    [-1, -1, -1]]
        self.assertEqual(expected, res)

    def test_7(self):
        a = [[0, 2, -1],
             [0, -1, -1],
             [0, -1, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[2, 1, -1],
                    [0, -1, -1],
                    [0, -1, -1]]
        self.assertEqual(expected, res)

    def test_8(self):
        a = [[-2, 2, -1],
             [-2, -1, -1],
             [-1, -1, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[3, 2, -1],
                    [-2, -1, -1],
                    [-1, -1, -1]]
        self.assertEqual(expected, res)

    def test_9(self):
        a = [[-100, -100, -100],
             [-100, -100, -100],
             [-100, -100, -100]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[-100, -100, -100],
                    [-100, -100, -100],
                    [-100, -100, -100]]
        self.assertEqual(expected, res)

    def test_10(self):
        a = [[-2, -1, 0]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[-2, -1, 0]]
        self.assertEqual(expected, res)

    def test_11(self):
        a = [[-2],
             [0],
             [24]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[-2],
                    [0],
                    [0]]
        self.assertEqual(expected, res)

    def test_12(self):
        a = [[-2, 24, 4, -29],
             [-1, 24, 0, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[25, 24, 4, -29],
                    [-1, 24, 0, -1]]
        self.assertEqual(expected, res)

    def test_13(self):
        a = [[5, 24, 4, -29],
             [-1, 24, 0, -1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, 0, 0, -29],
                    [-1, 0, 0, -1]]
        self.assertEqual(expected, res)

    def test_14(self):
        a = [[-2, 7],
             [0, 5],
             [24, 25]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[-2, 0],
                    [0, 0],
                    [0, 0]]
        self.assertEqual(expected, res)

    def test_15(self):
        a = [[0, -3, 1]]
        res = tasks.dashieva_Ykehev_mansheev(a)
        expected = [[0, -3, 1]]
        self.assertEqual(expected, res)

    def test_16(self):
        a = [[1, -12, 0],
             [4, 6, -8],
             [-1, 10, -1]]
        res = tasks.dashieva(a)
        expected = [[1, -12, -2],
                    [4, 6, -8],
                    [-1, 10, -1]]
        self.assertEqual(expected, res)

    def test_17(self):
        a = [[4, 2, 2],
             [-1, 2, -1],
             [12, 3, -1]]
        res = tasks.dashieva(a)
        expected = [[4, 2, 2],
                    [-1, 2, -1],
                    [12, 3, -1]]
        self.assertEqual(expected, res)

    def test_18(self):
        a = [[1, -2, 4, 29],
             [3, 4, 1, 1]]
        res = tasks.dashieva(a)
        expected = [[1, -2, 4, 29],
                    [3, 4, 1, 1]]
        self.assertEqual(expected, res)

    def test_19(self):
        a = [[1, 4, 0, 12],
             [-5, 8, 9, 0],
             [-6, 7, 0, 19]]

        count = 0
        for row in a:
            for elem in row:
                if elem == 0:
                    count += 1

        count -= 1

        res = tasks.dashieva(a)

        expectedCount = 0
        for row in res:
            for elem in row:
                if elem == 0:
                    expectedCount += 1

        self.assertEqual(expectedCount, count)

    def test_20(self):
        a = [[1, 4, 0, 12],
             [-5, 2, 30, 0],
             [-6, 4, 25, 19],
             [-7, 7, 0, 4],
             [-10, 7, 0, 14]]

        count = 0
        for row in a:
            for elem in row:
                if elem == 0:
                    count += 1

        count -= 1

        res = tasks.dashieva(a)

        expectedCount = 0
        for row in res:
            for elem in row:
                if elem == 0:
                    expectedCount += 1

        self.assertEqual(expectedCount, count)


if __name__ == '__main__':
    unittest.main()
