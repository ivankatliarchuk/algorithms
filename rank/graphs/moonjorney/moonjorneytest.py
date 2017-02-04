import sys
import unittest
import moonjorney


class Test(unittest.TestCase):

    def test_function(self):
        sys.stdin = open("simple.txt")
        countries = moonjorney.readCountries()
        print("from input {0}\n  fixtures {1}".format(countries, self.test_county))
        self.assertEqual(self.test_county, countries, 'not equal')

    def setUp(self):
        # raw_input is untouched before test
        self.test_county = {}
        self.orig_stdin = sys.stdin
        self.test_county[0] = {1, 2, 8}
        self.test_county[1] = {3, 9, 7}
        self.test_county[4] = {99, 11}
        self.test_county[5] = {6, 10}

    def tearDown(self):
        sys.stdin = self.orig_stdin
        self.test_country = {}

if __name__ == '__main__':
    unittest.main()
