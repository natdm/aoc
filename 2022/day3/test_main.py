import unittest
import main


class TestMain(unittest.TestCase):
    def test_score(self):
        self.assertEqual(main.score("a"), 1)
        self.assertEqual(main.score("z"), 26)
        self.assertEqual(main.score("A"), 27)
        self.assertEqual(main.score("Z"), 52)

    def test_split(self):
        self.assertEqual(main.half("abcdef"), ("abc", "def"))

    def test_p_sum(self):
        input = ("AbBcD", "eFgAx")
        self.assertEqual(main.p_sum(input), main.score("A"))

    def test_run(self):
        input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
            "\n"
        )
        self.assertEqual(main.run(input), 157)
