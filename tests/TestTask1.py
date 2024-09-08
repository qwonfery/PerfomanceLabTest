import unittest
from task1.task1 import get_path


class TestTask1(unittest.TestCase):
    def test1(self):
        path = get_path(4, 3)
        self.assertEqual(path, [1, 3])

    def test2(self):
        path = get_path(5, 4)
        self.assertEqual(path, [1, 4, 2, 5, 3])


if __name__ == '__main__':
    unittest.main()
