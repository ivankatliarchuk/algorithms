import sys
import unittest
from timeit import default_timer as timer
import equals


class Test(unittest.TestCase):
    def test(self):
        sys.stdin = open("test0.txt")
        start = timer()
        equals.readSteps()
        end = timer()
        print("{} seconds".format(end - start))
        """
        10605
        8198
        18762
        16931
        5104
        """
        #     average time 1.3 sec

    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
