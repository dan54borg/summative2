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
        result = self.app.display_output("John")
        self.assertEqual(result, "OK")

    def test_name_happy_edge(self):
        result = self.app.display_output("O'Toole")
        self.assertEqual(result, "OK")

      
    
if __name__ == "__main__":
    unittest.main()
