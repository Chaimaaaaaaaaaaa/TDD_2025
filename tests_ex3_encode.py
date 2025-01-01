import unittest
from ex3_encode import Encode  

class TestEncode(unittest.TestCase):
    
    def test_encode_text(self):
        cesar = Encode(3)
        self.assertEqual(cesar.encode_text("Hello, World!"), "Khoor, Zruog!")
        self.assertEqual(cesar.encode_text("1234!"), "1234!")
        self.assertEqual(cesar.encode_text(""), "")

if __name__ == "__main__":
    unittest.main()