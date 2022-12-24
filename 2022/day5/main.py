# https://adventofcode.com/2022/day/5


class Move:
    ct: int
    fro: int
    to: int

    def __init__(self, ct, fro, to):
        self.ct = ct
        self.fro = fro
        self.to = to


# parses a move, "move n from n to n"
def parse_move(move: str) -> Move:
    res = move.strip().split(" ")
    return Move(int(res[1]), int(res[3]), int(res[5]))


# crates should be a list of lists,
# [["A", "B", "C"], ["D", "E", "F"], etc.]
# moves should be a list of strings with a specific format.
def run(crates: list[list[str]], moves: str) -> str:
    _moves = list(map(parse_move, moves.strip().split("\n")))
    for move in _moves:
        fro = crates[move.fro - 1]
        for _ in range(move.ct):
            popped = fro.pop(len(fro) - 1)
            crates[move.to - 1].append(popped)

    output = ""
    for c in crates:
        output += c[len(c) - 1]

    return output
