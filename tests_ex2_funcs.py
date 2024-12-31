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
        
    # Tests LIFO
    def tests_LIFO(self):
        lifo = ex2_funcs.LIFO()
        self.assertTrue(lifo.is_empty())
        self.assertEqual(lifo.len(), 0)
        lifo.add(1)
        self.assertEqual(lifo.len(), 1) 
        lifo.add(2)
        self.assertEqual(lifo.len(), 2)
        lifo.add(3)
        self.assertEqual(lifo.len(), 3)
        self.assertFalse(lifo.is_empty())
        self.assertEqual(lifo.rmv(), 3)
        self.assertEqual(lifo.rmv(), 2)
        self.assertEqual(lifo.rmv(), 1)
    
    def test_rmv_empty(self):    
        with self.assertRaises(IndexError) as context:
            fifo = ex2_funcs.FIFO()
            fifo.rmv()
        self.assertEqual(str(context.exception), "empty")
        
        with self.assertRaises(IndexError) as context:
            lifo = ex2_funcs.LIFO()
            lifo.rmv()
        self.assertEqual(str(context.exception), "empty")
            
    
    
if __name__ == '__main__':
    unittest.main()