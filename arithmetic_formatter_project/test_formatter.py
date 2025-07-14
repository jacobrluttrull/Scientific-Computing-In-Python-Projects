import unittest
from formatter import arithmetic_arranger  # adjust if your file name is different

class TestArithmeticArranger(unittest.TestCase):

    def test_valid_problems(self):
        result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
        expected = "  32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    -----"
        self.assertEqual(result, expected)

    def test_too_many_problems(self):
        result = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        self.assertEqual(result, "Error: Too many problems.")

    def test_invalid_operator(self):
        result = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        self.assertEqual(result, "Error: Operator must be '+' or '-'.")

    def test_too_many_digits(self):
        result = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        self.assertEqual(result, "Error: Numbers cannot be more than four digits.")

    def test_non_digit_input(self):
        result = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        self.assertEqual(result, "Error: Numbers must only contain digits.")

    def test_with_answers(self):
        result = arithmetic_arranger(["3 + 855", "988 + 40"], True)
        expected = "    3      988\n+ 855    +  40\n-----    -----\n  858     1028"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

