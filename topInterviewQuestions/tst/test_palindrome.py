import unittest
from palindrome import Palindrome


class Palindrome_test(unittest.TestCase):
    def canary_test(self):
        self.assertEqual(True, True)

    def palindrome_test(self):
        obj = Palindrome
        result = obj.palindrome('121')
        self.assertEqual(result, 11)

    def palindrome_is_int(self):
        obj = Palindrome
        try:
            result = obj.palindrome('god')
        except:
            print('enter numbers only')
