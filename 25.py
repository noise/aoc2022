#!/usr/bin/env python3

"""
--- Day 25: Full of Hot Air ---
"""

import math

c2d = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
d2c = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}


def parse(inps):
    return inps.split("\n")


def sum(lines):
    # pad out and convert to numbers
    sums = [0] * 21
    for l in lines:
        l = str(l).zfill(21)
        for i in range(21):
            sums[i] += c2d[l[i]]

    # shift up
    sums = [s + 2 for s in sums]

    # carry and borrow until all clear
    while any([s > 4 or s < 0 for s in sums]):
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] > 4:  # carry
                c = int(sums[i] // 5)
                sums[i - 1] += c
                sums[i] = sums[i] % 5
            elif sums[i] < 0:  # borrow
                b = int(abs(sums[i]) // 5) + 1
                sums[i - 1] -= b
                sums[i] += b * 5

    # shift down
    sums = [s - 2 for s in sums]
    # back to snafu chars
    sums = [d2c[d] for d in sums]
    return "".join(sums)


def snafu2dec(snafu):
    val = 0
    for i in range(len(snafu) - 1, -1, -1):
        c = snafu[i]
        place = len(snafu) - i - 1
        pow = math.pow(5, place)
        dig = dig2d[digits.index(c)]
        # print(f"{i}: place: {place}, dig: {c} > {dig }")
        val += pow * dig
    return val


def one(inp):
    lines = parse(inp)
    return sum(lines)


sinp = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

inp = open("25.txt").read().strip()

print("1-sample:", one(sinp))  # 4890, snafu=2=-1=0
print("1-real:", one(inp))  # 2=020-===0-1===2=020
