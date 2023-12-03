import unittest
import main


class TestMain(unittest.TestCase):
    def test_run(self):
        input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split(
            "\n"
        )
        self.assertEqual(main.run(input), 2)
