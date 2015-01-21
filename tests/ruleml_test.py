__author__ = 'mpetyx'

import unittest

def multiply(x,y):
    return x*y

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)

    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')

    def test_kati(self):
        self.assertEqual(1,2)

if __name__ == '__main__':
    unittest.main()