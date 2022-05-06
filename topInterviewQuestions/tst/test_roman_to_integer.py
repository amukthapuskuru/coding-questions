import unittest
from roman_to_integer import RomanToInteger


class RomanToIntegerTest(unittest.TestCase):
    def canary_test(self):
        self.assertEqual(True, True)

    def test_roman_to_integer(self):
        obj = RomanToInteger
        result = obj.romanToInt('XCI')
        self.assertEqual(result, 9)


    def test_roman_to_integer_if_int_is_passed(self):
        obj = RomanToInteger
        try:
            result = obj.romanToInt(10)
        except:
            print("Enter valid alphabets only")


if __name__ == '__main__':
    unittest.main()
