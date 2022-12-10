#!/usr/bin/env python3

"""
--- Day 10: Cathode-Ray Tube ---
"""


def render(crt):
    print("\n".join(["".join(crt[i : i + 40]) for i in range(0, 240, 40)]))


def clock(insts):
    # expand to clock
    ticks = []
    for i in insts:
        if i.startswith("addx"):
            ticks.append("nope")
        ticks.append(i)

    crt = ["."] * 240
    pc = 0
    x = 1
    sums = 0
    while pc < len(ticks):
        i = ticks[pc]

        # draw
        crt[pc] = "#" if pc % 40 in range(x - 1, x + 2) else "."

        # check clock, signal strengths
        pc += 1
        sums += pc * x if pc in [20, 60, 100, 140, 180, 220] else 0

        # increment register at end of cycle
        if i.startswith("addx"):
            x += int(i.split(" ")[1])

    render(crt)
    return pc, x, sums


inp = open("10s.txt").read().strip().split("\n")
print(clock(inp))  # 13140

inp = open("10.txt").read().strip().split("\n")
print(clock(inp))  # 13740, XUPRFECL
