import unittest # importing the testing framework
from unittest.mock import patch 
from main import KnifeSafety

class SmokeTest(unittest.TestCase):
    def setUp(self): 
        self.app = KnifeSafety() 
    
    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertTrue(1)
        self.assertFalse(0)
    
    def test_name_happy(self):
        #Testing names are accepted
        result = self.app.display_output("John")
        self.assertEqual(result, "OK")

    def test_name_happy_edge(self):
        #Testing that characters are accepted
        result = self.app.display_output("O'Toole")
        self.assertEqual(result, "OK")
        #Testing the length of a name
        result = self.app.display_output("Christopher Walken")
        self.assertEqual(result,"OK")
        result = self.app

    @patch('tkinter.messagebox.showerror') 
    def test_name_fail_presence(self, mock_error):
        #Testing that leaving the name blank will show up the correct error
        self.app.display_output("")
        mock_error.assert_called_with("Error", "Name cannot be left blank")
        #Testing the error for characters
        self.app.display_output("Dan1el")
        mock_error.assert_called_with("Error", "The name should not have any numbers")
         



      
    
if __name__ == "__main__":
    unittest.main()
