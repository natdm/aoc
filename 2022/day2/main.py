# https://adventofcode.com/2022/day/2
import sys


# Convert possible inputs to constants just for programming ease
class Moves:
    A = "A"
    B = "B"
    C = "C"
    X = "X"
    Y = "Y"
    Z = "Z"
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"


def typed(v: (str, str)) -> (Moves, Moves):
    def _typed(vv: str) -> Moves:
        match vv:
            case Moves.A | Moves.X:
                return Moves.Rock
            case Moves.B | Moves.Y:
                return Moves.Paper
            case Moves.C | Moves.Z:
                return Moves.Scissors
            case _:
                raise Exception("no")

    return (_typed(v[0]), _typed(v[1]))


def score(value: (str, str)) -> (int, int):
    base_pt = 0
    v = typed(value)
    # add the points you might win as a bonus, for the move you chose
    match v[1]:
        case Moves.Rock:
            base_pt = 1
        case Moves.Paper:
            base_pt = 2
        case Moves.Scissors:
            base_pt = 3

    match typed(value):
        case (Moves.Scissors, Moves.Paper) | (Moves.Rock, Moves.Scissors) | (
            Moves.Paper,
            Moves.Rock,
        ):
            return (6, 0 + base_pt)
        case (Moves.Paper, Moves.Scissors) | (Moves.Scissors, Moves.Rock) | (
            Moves.Rock,
            Moves.Paper,
        ):
            return (0, 6 + base_pt)
        case x:
            return (3, 3 + base_pt)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("need a file, eg: python main.py input.txt")
    f = open(sys.argv[1])
    input = f.readlines()

    total = 0
    for l in input:
        s = score(tuple(l.strip().split(" ")))
        total += s[1]

    print(total)
