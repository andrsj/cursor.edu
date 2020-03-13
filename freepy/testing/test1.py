import unittest
from main1 import check_pass


class TestCheckPass(unittest.TestCase):
    def test_len(self):
        except_res = False
        actual_res = check_pass("asdfghjklaa")
        self.assertEqual(except_res,actual_res)

    def test_check(self):
        except_res = True
        actual_res = check_pass("Asdfghjkl0")
        self.assertEqual(except_res,actual_res)


if __name__ == "__main__":
    unittest.main()