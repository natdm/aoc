# https://adventofcode.com/2022/day/6


# find the first index where the four previous characters are all different.
def run(input: str) -> int:
    print(input)
    x = list(input)

    left, right = 0, 1
    while right <= len(x):
        print("{} | {}".format(x[left:right], x[right + 1]))
        if str(x[left:right]).find(x[right + 1]) > 0:
            if right > 3:
                left += 1
            right += 1
        elif left > 4:
            return right
        else:
            if right > 4:
                left += 1
            right += 1

    # for i in range(4, len(x)):
    #     print("{} contain {} ?".format(x[i - 4 : i], x[i]))
    #     if str(x[i - 4 : i]).find(x[i]) < 0:
    #         print("no")
    #         return i + 1
    #     print("yes")

    return -1
