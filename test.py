import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(2, 2), 0)


if __name__ == 'main':
    unittest.main()
