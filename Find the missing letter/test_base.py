import unittest
from base import find_missing_letter

class TestBase(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')

if __name__ == '__main__':
    unittest.main()