# https://adventofcode.com/2022/day/3


def score(c: str) -> int:
    o = ord(c)

    if o >= ord("A") and o <= ord("Z"):
        return o - ord("A") + 27
    if o >= ord("a") and o <= ord("z"):
        return o - ord("a") + 1

    return -1


def half(v: str) -> tuple[str, str]:
    return (v[: len(v) // 2], v[len(v) // 2 :])


def p_sum(v: tuple[str, str]) -> int:
    # keep track of if the value was found
    # in the left and/or right hand side of
    # the bag
    m: dict[str, tuple[bool, bool]] = {}

    for i in v[0]:
        m[i] = (True, False)

    for i in v[1]:
        vv = m.get(i, (False, False))
        _vv = (vv[0], True)
        m[i] = _vv

    top = 0

    for i in m:
        if m[i] != (True, True):
            continue

        current_score = score(i)
        if current_score > top:
            top = current_score

    return top


def run(input: list[str]) -> int:
    total = 0
    for i in input:
        total += p_sum(half(i))

    return total
