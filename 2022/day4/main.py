# https://adventofcode.com/2022/day/4


def run(input: list[str]) -> int:
    overlaps = 0
    for i in input:
        match i.strip().split(","):
            case [left, right]:
                lrange = left.split("-")
                rrange = right.split("-")
                if ord(lrange[0]) <= ord(rrange[0]) and ord(lrange[1]) >= ord(
                    rrange[1]
                ):
                    overlaps += 1
                if ord(lrange[0]) >= ord(rrange[0]) and ord(lrange[1]) <= ord(
                    rrange[1]
                ):
                    overlaps += 1
            case _:
                raise Exception("incorrect pattern")

    return overlaps
