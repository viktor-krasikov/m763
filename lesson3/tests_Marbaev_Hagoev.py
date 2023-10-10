import unittest
import tasks


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = [[1, 2, 0],
             [4, 6, 8],
             [-5, 0, -1]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[0, 0, 8],
                    [0, 0, 0],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_2(self):
        a = [[1, 2, -1],
             [4, 6, 8],
             [-5, 0, -1]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[0, 0, -1],
                    [0, 0, 0],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_3(self):
        a = [[1, 2, -2],
             [4, 6, 8],
             [-5, 0, -1]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[1, 2, 9],
                    [4, 6, 8],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_4(self):
        a = [[1, 10, -1],
             [4, 6, 8],
             [-5, 0, -1]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[0, 0, -1],
                    [0, 0, 0],
                    [-5, 0, -1]]
        self.assertEqual(expected, a)

    def test_5(self):
        a = [[1, 2, -1]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[0, 0, -1]]
        self.assertEqual(expected, a)

    def test_6(self):
        a = [[1, 2],
             [4, 6],
             [-5, 0]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[1, 2],
                    [4, 6],
                    [-5, 0]]
        self.assertEqual(expected, a)

    def test_7(self):
        a = [[-1, -2],
             [6, 6],
             [-5, 0]]
        tasks.Marbaev_Hagoev_Panteleev(a)
        expected = [[-1, -2],
                    [0, 0],
                    [-5, 0]]
        self.assertEqual(expected, a)




if __name__ == '__main__':
    unittest.main()
