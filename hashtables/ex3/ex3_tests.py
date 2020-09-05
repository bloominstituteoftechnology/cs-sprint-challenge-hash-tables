import unittest

from ex3 import intersection


class TestEx2(unittest.TestCase):

    def test_small(self):
        result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1,2],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1,2,3],
            [1,4,5,3],
            [1,6,7,3]
        ])
        result.sort()
        self.assertTrue(result == [1,3])

    def test_large(self):
        arrays = [
            list(range(100000, 200000)) + [1,2,3],
            list(range(200000, 300000)) + [1,2,3],
            list(range(300000, 400000)) + [1,2,3],
            list(range(400000, 500000)) + [1,2,3],
            list(range(500000, 600000)) + [1,2,3],
            list(range(600000, 700000)) + [1,2,3],
            list(range(700000, 800000)) + [1,2,3],
            list(range(800000, 900000)) + [1,2,3],
            list(range(900000, 1000000)) + [1,2,3],
            list(range(1000000, 1100000)) + [1,2,3]
        ]

        result = intersection(arrays)
        result.sort()
        self.assertTrue(result == [1,2,3])

if __name__ == '__main__':
    unittest.main()
