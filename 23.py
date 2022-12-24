#!/usr/bin/env python3

"""
--- Day 23: Unstable Diffusion ---
"""
import re
from itertools import cycle

RENDER = True


def pboard(elves):
    if RENDER:
        for j in range(100):
            l = ["#" if (i, j) in elves else "." for i in range(100)]
            print("".join(l))
        #input()


def parse(inp):
    return {
        (x, y)
        for y, l in enumerate(inp.split("\n"))
        for x, e in enumerate(l)
        if e == "#"
    }



checks = {
    (0, -1): [(-1, -1), (0, -1), (1, -1)],  # N
    (0, 1): [(-1, 1), (0, 1), (1, 1)],  # S
    (-1, 0): [(-1, -1), (-1, 0), (-1, 1)],  # W
    (1, 0): [(1, -1), (1, 0), (1, 1)],  # E
}
alldir = list(set([c for cs in checks.values() for c in cs]))


def check_prop(elves, e, chk):
    # true if no collision
    return (len(set(elves).intersection(set([(e[0] + c[0], e[1] + c[1]) for c in chk]))) == 0)


def all_empty(elves, e):
    # len(set(elves).intersection(set([(e[0]+c[0], e[1] + c[1]) for c in alldir]))) == 0
    for d in alldir:
        if (e[0] + d[0], e[1] + d[1]) in elves:
            return False
    return True


def sim(elves, rounds, two):
    moves = cycle([(0, -1), (0, 1), (-1, 0), (1, 0)])
    if two:
        rounds = 10000
    for i in range(rounds):
        pboard(elves)

        round_moves = [next(moves) for _ in range(4)]

        # proposals first
        props = {}
        for e in elves:
            if all_empty(elves, e):
                continue
            for m in round_moves:
                chk = checks[m]
                if empty := check_prop(elves, e, chk):
                    prop = (e[0] + m[0], e[1] + m[1])
                    if prop in props:
                        if props[prop] != "nope":
                            props[prop] = "nope"
                    else:
                        props[prop] = e
                    break

        # check part 2 exit
        if i % 50 == 0:
            print(i)
        if two and len(props) == 0:
            return i + 1

        # then move elves
        for prop, e in props.items():
            if e != "nope":
                elves.remove(e)
                elves.add(prop)
        next(moves)  # burn one before next round

    # empty ground within the elves bounding rect
    sx = max([e[0] for e in elves]) + 1 - min([e[0] for e in elves])
    sy = max([e[1] for e in elves]) + 1 - min([e[1] for e in elves])
    return sx * sy - len(elves)


def one(inp, two=False):
    elves = parse(inp)
    return sim(elves, 10, two)


sinp = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

sinp2 = """.....
..##.
..#..
.....
..##.
....."""


inp = open("23.txt").read().strip()

print("1-sample:", one(sinp))  # 110
print("1-real:", one(inp))  # 3800

print("2-sample:", one(sinp, True))  # 20
print("2-real:", one(inp, True))  # 916
