import unittest
import main


class TestMain(unittest.TestCase):
    def test_parse_move(self):
        res = main.parse_move("move 5 from 1 to 2")
        self.assertEqual(res.ct, 5)
        self.assertEqual(res.fro, 1)
        self.assertEqual(res.to, 2)

        input = """
        move 5 from 1 to 2
        move 1 from 3 to 4
        move 6 from 4 to 2
        """

        m = list(map(main.parse_move, input.strip().split("\n")))
        self.assertEqual(m[0].ct, 5)
        self.assertEqual(m[0].fro, 1)
        self.assertEqual(m[0].to, 2)
        self.assertEqual(m[2].ct, 6)
        self.assertEqual(m[2].fro, 4)
        self.assertEqual(m[2].to, 2)

    def test_run(self):
        input = """
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
        """
        self.assertEqual(
            main.run(
                [
                    ["Z", "N"],
                    ["M", "C", "D"],
                    ["P"],
                ],
                input,
            ),
            "CMZ",
        )


if __name__ == "__main__":
    unittest.main()
