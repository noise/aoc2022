#!/usr/bin/env python3

"""
--- Day 9: Rope Bridge ---
"""

import numpy as np


dirs = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}


def parse(inp):
    return [(dirs[m[0]], int(m[1])) for m in [l.split(" ") for l in inp.strip().split("\n")]]


def sim(moves):
    trail = {"0, 0": 1}
    h = [0, 0]
    t = [0, 0]
    for d, n in moves:
        for i in range(n):
            h = np.add(h, d)
            # chase
            offset = np.subtract(h, t)
            if abs(offset[0]) > 1 or abs(offset[1]) > 1:
                t = np.add(t, np.multiply(np.sign(offset), [1, 1]))
                trail[str(t)] = 1
    print(len(trail))


def sim2(moves):
    trail = {"0,0": 1}
    knots = [[0, 0] for _ in range(10)]
    print(knots)
    for d, n in moves:
        for i in range(n):
            knots[0] = np.add(knots[0], d)
            # chase
            for k in range(1, 10):
                offset = np.subtract(knots[k - 1], knots[k])
                if abs(offset[0]) > 1 or abs(offset[1]) > 1:
                    knots[k] = np.add(knots[k], np.multiply(np.sign(offset), [1, 1]))
                    if k == 9:
                        trail[str(knots[9][0]) + "," + str(knots[9][1])] = 1
    print(len(trail))


moves = parse(
    """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
)

sim(moves)  # 13
sim2(moves)  # 1

moves = parse(
    """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
)
sim2(moves)  # 36

moves = parse(open("9.txt").read())
sim(moves)  # 6098
sim2(moves)  # 2597
