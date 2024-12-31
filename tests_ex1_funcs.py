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
    
    def test_is_prime_number(self):
        self.assertTrue(ex1_funcs.is_prime_number(2))
        self.assertTrue(ex1_funcs.is_prime_number(3))
        self.assertTrue(ex1_funcs.is_prime_number(5))
        self.assertTrue(ex1_funcs.is_prime_number(7))
        self.assertTrue(ex1_funcs.is_prime_number(11))
        self.assertFalse(ex1_funcs.is_prime_number(1))
        self.assertFalse(ex1_funcs.is_prime_number(4))
        self.assertFalse(ex1_funcs.is_prime_number(6))
        self.assertFalse(ex1_funcs.is_prime_number(0))
        self.assertFalse(ex1_funcs.is_prime_number(-1))
        
    def test_is_arithmetic_sequence(self):
        self.assertTrue(ex1_funcs.is_arithmetic_sequence([1, 2, 3, 4, 5]))
        self.assertTrue(ex1_funcs.is_arithmetic_sequence([1, 3, 5, 7, 9]))
        self.assertTrue(ex1_funcs.is_arithmetic_sequence([1, 1, 1, 1, 1]))  
        self.assertTrue(ex1_funcs.is_arithmetic_sequence([1, 0, -1, -2, -3]))
        self.assertTrue(ex1_funcs.is_arithmetic_sequence([1, -1, -3, -5, -7]))
        self.assertFalse(ex1_funcs.is_arithmetic_sequence([1, 2, 3, 4, 6]))
        self.assertFalse(ex1_funcs.is_arithmetic_sequence([1, 3, 5, 7, 8]))
        self.assertFalse(ex1_funcs.is_arithmetic_sequence([1, 1, 1, 1, 2]))
        self.assertFalse(ex1_funcs.is_arithmetic_sequence([]))
        
    
if __name__ == '__main__':
    unittest.main()