# !!! Тести не впливають один на одного

# Unit tests
# Інтеграційні тести
# End to end tests

import unittest
from main import sum_of_inter, sum_of_arg


class TestSum(unittest.TestCase):
    def test_with_two_init(self):
        exepted_result = 3
        actual_result = sum_of_inter(1, 2)
        self.assertEqual(exepted_result, actual_result, "1 + 2")

    def test_with_string(self):
        exepted_result = 'lk'
        actual_result = sum_of_inter('l','k')
        self.assertEqual(exepted_result, actual_result, "l + k")

    def test_with_args(self):
        exepted_result = 6
        actual_result = sum_of_arg(1,2,3)
        self.assertEqual(exepted_result, actual_result, "1,2,3")

if __name__ == "__main__":
    unittest.main()