import ex1_funcs
import unittest

class TestEx1Funcs(unittest.TestCase):
    def test_max_three_ints(self):
        self.assertEqual(ex1_funcs.max_three_ints(0, 1, 2), 2)
        self.assertEqual(ex1_funcs.max_three_ints(1, 3, 2), 3)
        self.assertEqual(ex1_funcs.max_three_ints(3, 1, 2), 3)
        self.assertEqual(ex1_funcs.max_three_ints(1, 1, 1), 1)
        self.assertEqual(ex1_funcs.max_three_ints(-1, -2, -3), -1)
        self.assertEqual(ex1_funcs.max_three_ints(-1, 2, -3), 2)
    
if __name__ == '__main__':
    unittest.main()