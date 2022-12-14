#!/usr/bin/env python3

"""
--- Day 14: Regolith Reservoir ---

"""
from collections import defaultdict
from itertools import pairwise
import os
import numpy as np


def parse(inps):
    rocklines = [list(map(eval, l.split(" -> "))) for l in inps.split("\n")]
    return [list(pairwise(r)) for r in rocklines]


def render(cave, floor):
    if not RENDER:
        return
    os.system("clear")
    for y in range(0, floor + 5):
        print("".join([cave[(x, y)] for x in range(300, 700)]))


def drawrocks(cave, rocks, two):
    maxy = 0
    for line in rocks:
        for (p1, p2) in line:
            maxy = max([p1[1], p2[1], maxy])
            if p1[0] == p2[0]:
                for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                    cave[(p1[0], y)] = "#"
            else:
                for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                    cave[(x, p1[1])] = "#"
    if two:
        for x in range(0, 1000):
            cave[x, maxy + 2] = "#"
    return maxy


dirs = [[0, 1], [-1, 1], [1, 1]]


def move1(cave, s):
    for d in dirs:
        tc = np.add(s, d)
        if cave[tuple(tc)] == ".":
            cave[tuple(s)] = "."
            s = tc
            cave[tuple(s)] = "o"
            return False, s
    return True, s  # at rest


def dropsand(cave, s, floor):
    rest = False
    while not rest:
        rest, s = move1(cave, s)
        if s[1] >= floor or s[1] == 0:  # abyss or source
            return False
    # render(cave, floor)
    # input()
    return True


def sim(inps, two=False):
    cave = defaultdict(lambda: ".")
    rocklines = parse(inps)
    floor = drawrocks(cave, rocklines, two)
    render(cave, floor)

    grains = 0
    while True:
        s = (500, 0)
        rest = dropsand(cave, s, floor + 2)
        if not rest:
            break
        grains += 1
        # if  grains % 100 == 0:
        render(cave, floor)
    return grains


RENDER = False

sinp = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

print(sim(sinp, False))  # 24
print(sim(sinp, True) + 1)  # 93

inp = open("14.txt").read().strip()
print(sim(inp, False))  # 961
print(sim(inp, True) + 1)  # 26375
