import unittest
import main


class TestMain(unittest.TestCase):
    def test_run(self):
        self.assertEqual(main.run("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(main.run("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(main.run("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(main.run("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)


if __name__ == "__main__":
    unittest.main()
