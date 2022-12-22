# https://adventofcode.com/2022/day/2
import sys


# Convert possible inputs to constants just for programming ease
class M:
    A = "A"
    B = "B"
    C = "C"
    X = "X"
    Y = "Y"
    Z = "Z"
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"


def typed(v: tuple[str, str]) -> tuple[str, str]:
    def _typed(vv: str) -> str:
        match vv:
            case M.A | M.X:
                return M.Rock
            case M.B | M.Y:
                return M.Paper
            case M.C | M.Z:
                return M.Scissors
            case _:
                raise Exception("no")

    return (_typed(v[0]), _typed(v[1]))


def score(value: tuple[str, str]) -> tuple[int, int]:
    base_pt = 0
    v = typed(value)
    # add the points you might win as a bonus, for the move you chose
    match v[1]:
        case M.Rock:
            base_pt = 1
        case M.Paper:
            base_pt = 2
        case M.Scissors:
            base_pt = 3

    match typed(value):
        case (M.Scissors, M.Paper) | (M.Rock, M.Scissors) | (M.Paper, M.Rock):
            return (6, 0 + base_pt)
        case (M.Paper, M.Scissors) | (M.Scissors, M.Rock) | (M.Rock, M.Paper):
            return (0, 6 + base_pt)
        case (x, y) if x == y:
            return (3, 3 + base_pt)
        case _:
            raise Exception("Impossibru!")


def calculate_score(input):
    total = 0
    for l in input:
        s = score(tuple(l.strip().split(" ")))
        total += s[1]

    return total
