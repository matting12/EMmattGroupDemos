import unittest
from week2_Monday_demo_calc import add, subtract, multiply, divide

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11)
    
    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
    
    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "main":
    unittest.main()
