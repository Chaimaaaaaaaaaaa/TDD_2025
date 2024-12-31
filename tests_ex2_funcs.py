import ex2_funcs
import unittest

class TestEx2Funcs(unittest.TestCase):
    # Tests FIFO
    def tests_FIFO(self):
        fifo = ex2_funcs.FIFO()
        self.assertTrue(fifo.is_empty())
        self.assertEqual(fifo.len(), 0)
        fifo.add(1)
        self.assertEqual(fifo.len(), 1) 
        fifo.add(2)
        self.assertEqual(fifo.len(), 2)
        fifo.add(3)
        self.assertEqual(fifo.len(), 3)
        self.assertFalse(fifo.is_empty())
        self.assertEqual(fifo.rmv(), 1)
        self.assertEqual(fifo.rmv(), 2)
        self.assertEqual(fifo.rmv(), 3)
        
        
    
    
    
if __name__ == '__main__':
    unittest.main()