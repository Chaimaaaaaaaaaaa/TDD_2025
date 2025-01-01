import unittest
from ex3_encode import Encode  
from unittest.mock import patch

class TestEncode(unittest.TestCase):
    
    def test_encode_text(self):
        cesar = Encode(3)
        self.assertEqual(cesar.encode_text("Hello, World!"), "Khoor, Zruog!")
        self.assertEqual(cesar.encode_text("1234!"), "1234!")
        self.assertEqual(cesar.encode_text(""), "")
        cesar_neg = Encode(-3)
        self.assertEqual(cesar_neg.encode_text("Khoor, Zruog!"), "Hello, World!")
            
    @patch('builtins.input', side_effect=["chiffre de cesar", "10"])  # Simule l'entrée utilisateur
    @patch('builtins.print')  # Capture la sortie print
    def test_main_function(self, mock_print, mock_input):
        
        from ex3_encode import main
        main()  
        
        mock_print.assert_called_with("Message secret: mrsppbo no mockb")
        
        mock_input.assert_any_call("Entrer le text à encoder: ")
        mock_input.assert_any_call("Entrer la valeur du shift: ")

if __name__ == "__main__":
    unittest.main()