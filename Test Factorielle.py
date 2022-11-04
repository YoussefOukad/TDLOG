import unittest
import Factorielle
import math

class MyTestCase(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(Factorielle.factoriell(6), math.factorial(6))  # add assertion here

if __name__ == '__main__':
    unittest.main()
