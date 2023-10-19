import unittest
import tasks

class MyTestCase(unittest.TestCase):
    def test1(self):
        a=[[1,2,3],
           [4,5,6],
           [7,8,5],]
        res=tasks.can_not_step_down(a)
        expected = "True"
        self.assertEqual(expected, res)