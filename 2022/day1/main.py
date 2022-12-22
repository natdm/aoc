# Calorie Counting
# https://adventofcode.com/2023/day/1
import sys


def count_calories(elf_cal_ct):
    elf_idx_cal_ct = {}
    elf_ct = 1
    cal_ct = 0
    for idx, entry in enumerate(elf_cal_ct):
        if idx == len(elf_cal_ct) - 1:
            cal_ct += int(entry)
            elf_idx_cal_ct["elf {}".format(elf_ct)] = cal_ct
        elif entry == "\n":
            elf_idx_cal_ct["elf {}".format(elf_ct)] = cal_ct
            elf_ct += 1
            cal_ct = 0
        else:
            cal_ct += int(entry)

    return elf_idx_cal_ct


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("need a file, eg: python main.py input.txt")
    f = open(sys.argv[1])
    elf_cal_ct = f.readlines()
    elf_cals = count_calories(elf_cal_ct)
    highest_ct = 0
    highest_name = ""
    for elf in elf_cals:
        if elf_cals[elf] > highest_ct:
            highest_name = elf
            highest_ct = elf_cals[elf]

    print(highest_name)
