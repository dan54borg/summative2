import unittest # importing the testing framework
from unittest.mock import patch 


class SmokeTest(unittest.TestCase):
    def setUp(self): 
        self.app = () 
    
    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertTrue(1)
        self.assertFalse(0)
    
  

    
if __name__ == "__main__":
    unittest.main()
