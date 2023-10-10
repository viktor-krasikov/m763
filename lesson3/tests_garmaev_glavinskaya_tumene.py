import unittest
import tasks


class MyTestCase(unittest.TestCase):
    def test_last_el_matrix1(self):
        a = [[1, 2, 0],
             [4, 6, 8],
             [-5, 10, -1]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_last_el_matrix2(self):
        a = [[1, 2, 0, 12],
             [4, 6, 8, -16],
             [-5, 0, -1, 4],
             [15, 0, 48, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0, 0],
                    [0, 0, 0, -16],
                    [-5, 0, -1, 0],
                    [0, 0, 0, 0]]
        self.assertEqual(expected, a)

    def test_last_el_matrix3(self):
        a = [[1, 2, 0],
             [4, -6, 18]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [0, -6, 0]]
        self.assertEqual(expected, a)

    def test_down_neg1_matrix1(self):
        a = [[1, 2, 0],
             [4, 6, 8],
             [-5, 0, -1]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_down_neg1_matrix2(self):
        a = [[1, 2, 0, 12],
             [4, 6, 48, -16],
             [-5, 0, -1, 4],
             [15, 0, 14, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0, 0],
                    [0, 0, 0, -16],
                    [-5, 0, -1, 0],
                    [0, 0, 0, 0]]
        self.assertEqual(expected, a)

    def test_down_neg1_matrix3(self):
        a = [[1, 22, 0],
             [4, -1, 18]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [0, -1, 0]]
        self.assertEqual(expected, a)

    def test_down_more1_matrix1(self):
        a = [[1, 2, 0],
             [4, 6, 18],
             [-5, 0, 7]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [0, 0, 0],
                    [-5, 0, 0]]
        self.assertEqual(expected, a)

    def test_down_more1_matrix2(self):
        a = [[1, 2, 0, 12],
             [4, 6, 48, -16],
             [-5, 0, 2, 4],
             [15, 0, 14, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0, 0],
                    [0, 0, 0, -16],
                    [-5, 0, 0, 0],
                    [0, 0, 0, 0]]
        self.assertEqual(expected, a)

    def test_down_more1_matrix3(self):
        a = [[1, 22, 0],
             [-4, 5, 18]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 0, 0],
                    [-4, 0, 0]]
        self.assertEqual(expected, a)

    def test_down_zero_matrix1(self):
        a = [[1, 2, 0],
             [4, 6, 8],
             [-5, 0, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 1, 0],
                    [3, 5, 7],
                    [-5, 0, 8]]
        self.assertEqual(expected, a)

    def test_down_zero_matrix2(self):
        a = [[1, 2, 0, 12],
             [4, 6, 48, -16],
             [-5, 0, 0, 4],
             [15, 0, 14, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 1, 0, 11],
                    [3, 5, 47, -16],
                    [-5, 0, 48, 3],
                    [14, 0, 13, 0]]
        self.assertEqual(expected, a)

    def test_down_zero_matrix3(self):
        a = [[1, 22, 0],
             [4, 0, 18]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[0, 21, 0],
                    [3, 22, 17]]
        self.assertEqual(expected, a)

    def test_down_neg2_matrix1(self):
        a = [[1, 2, 0],
             [4, 6, 8],
             [-5, 0, -2]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[1, 2, 0],
                    [4, 6, 8],
                    [-5, 0, 9]]
        self.assertEqual(expected, a)

    def test_down_neg2_matrix2(self):
        a = [[1, 2, 0, 12],
             [4, 6, 48, -16],
             [-5, 0, -2, 4],
             [15, 0, 14, 0]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[1, 2, 0, 12],
                    [4, 6, 48, -16],
                    [-5, 0, 49, 4],
                    [15, 0, 14, 0]]
        self.assertEqual(expected, a)

    def test_down_neg2_matrix3(self):
        a = [[1, 22, 0],
             [4, -2, 18]]
        tasks.garmaev_glavinskaya_tumene(a)
        expected = [[1, 22, 0],
                    [4, 23, 18]]
        self.assertEqual(expected, a)

    def test_pos_4_0_matrix1(self):
        a = [[-1, -2, 0, -12, -5],
             [-4, -6, 48, -16, -5],
             [-5, 0, -2, 0, -4],
             [-15, 0, -14, 0, -3]]
        result = tasks.garmaev_glavinskaya_tumene2(a)
        expected = [[-1, -2, 0, -12, -5],
                    [-4, -6, 48, -16, -5],
                    [-5, 0, -2, 0, -4],
                    [-15, 0, -14, 0, -3]]
        self.assertEqual(expected, a)
        self.assertFalse(result)

    def test_pos_4_0_matrix2(self):
        a = [[-1, -2, 0, -12, -5],
             [0, 0, 0, 0, -5],
             [-5, 0, -2, 0, -4],
             [-15, 0, -14, 0, -3]]
        result = tasks.garmaev_glavinskaya_tumene2(a)
        expected = [[-1, -2, 0, -12, -5],
                    [1, 2, 3, 0, -5],
                    [-5, 0, -2, 0, -4],
                    [-15, 0, -14, 0, -3]]
        self.assertEqual(expected, a)
        self.assertTrue(result)

    def test_pos_4_0_matrix3(self):
        a = [[-1, -2, 0, 0, -5],
             [0, -6, 0, 0, 0],
             [-5, 0, 0, 0, -4],
             [-15, 0, -14, 0, -3]]
        result = tasks.garmaev_glavinskaya_tumene2(a)
        expected = [[-1, -2, 0, 0, -5],
                    [0, -6, 0, 0, 0],
                    [-5, 0, 0, 0, -4],
                    [-15, 0, -14, 0, -3]]
        self.assertEqual(expected, a)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
