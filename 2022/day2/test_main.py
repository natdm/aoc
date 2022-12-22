import unittest
import main


class TestMain(unittest.TestCase):
    def test_calculate_score(self):
        result = main.calculate_score(["A Y\n", "B X\n", "C Z\n"])
        self.assertEqual(result, 15)

        result = main.calculate_score(["A X\n", "B X\n", "C Z\n"])
        self.assertEqual(result, 11)
