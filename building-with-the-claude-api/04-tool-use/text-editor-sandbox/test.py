"""
Test module for main.py functions
"""
import unittest
from main import greet, add, calculate_pi_5_digits


class TestMainFunctions(unittest.TestCase):
    """Test cases for functions in main.py"""
    
    def test_greet(self):
        """Test the greet function"""
        self.assertEqual(greet("world"), "Hello, world!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")
    
    def test_add(self):
        """Test the add function"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_calculate_pi_5_digits(self):
        """Test the calculate_pi_5_digits function"""
        pi_value = calculate_pi_5_digits()
        
        # Check that the result is a float
        self.assertIsInstance(pi_value, float)
        
        # Check that pi is approximately 3.14159 (pi to 5 decimal places)
        self.assertEqual(pi_value, 3.14159)
        
        # Check that pi is in the expected range
        self.assertGreater(pi_value, 3.14)
        self.assertLess(pi_value, 3.15)
        
        # Print the calculated value for verification
        print(f"Calculated pi to 5 decimal places: {pi_value}")


if __name__ == "__main__":
    unittest.main()
