import unittest
import main


class TestMain(unittest.TestCase):
    def test_run(self):
        result = main.run(["A Y\n", "B X\n", "C Z\n"])
        self.assertEqual(result, 15)

        result = main.run(["A X\n", "B X\n", "C Z\n"])
        self.assertEqual(result, 11)
