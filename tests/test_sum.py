# test of sum function

import unittest
from src import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data =[1, 2, 3]
        result = sum.sum_function(data)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()

