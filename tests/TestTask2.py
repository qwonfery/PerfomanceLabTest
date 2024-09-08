import unittest
from task2.task2 import find_locations


class MyTestCase(unittest.TestCase):
    def test1(self):
        locations = find_locations(5, [1, 1], [
            [0, 0],
            [1, 6],
            [6, 6]
        ])
        self.assertEqual(locations, ['1', '0', '2'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
