import unittest

from task4.task4 import find_min_moves


class MyTestCase(unittest.TestCase):
    def test1(self):
        moves = find_min_moves([1, 2, 3])
        self.assertEqual(moves, 2)  # add assertion here

    def test2(self):
        moves = find_min_moves([1, 10, 2, 9])
        self.assertEqual(moves, 16)  # add assertion here


if __name__ == '__main__':
    unittest.main()
