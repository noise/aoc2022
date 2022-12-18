#!/usr/bin/env python3

"""
--- Day 17: Pyroclastic Flow ---

"""
import os
from itertools import cycle


rocks = [
    [0b011110000],
    [0b001000000,
     0b011100000,
     0b001000000],
    [0b000100000,
     0b000100000,
     0b011100000],
    [0b010000000,
     0b010000000,
     0b010000000,
     0b010000000],
    [0b011000000,
     0b011000000],
]
rh = [1, 3, 3, 4, 2]


def bs(b):
    return "{:09b}".format(b)


def draw(space, rn, rx, ry, partial=True):
    if not RENDER:
        return
    rg = (range(max(0, ry - 5), min(ry + 10, len(space))) if partial else range(len(space)))
    for r in rg:
        if ry <= r < ry + rh[rn]:
            print(bs(space[r] | rocks[rn][r - ry] >> rx))
        else:
            print(bs(space[r]))
    print()
    print(f"stopped={stopped} - rn: {rn}, rx: {rx}, ry: {ry}")
    input()


def side_coll(space, rn, rx, ry, left):
    r = rocks[rn]
    for j in range(rh[rn]):
        if left:
            if space[ry + j] & (r[j] << 1 >> rx):
                return 0
        else:
            if space[ry + j] & (r[j] >> (1 + rx)):
                return 0
    return -1 if left else 1


def down_coll(space, rn, rx, ry):
    # bottom of rock vs next space line down
    if space[ry + rh[rn]] & (rocks[rn][-1] >> rx):
        return True
    # for 2nd line hit on rock #2
    if rn == 0:
        return False
    if space[ry + rh[rn] - 1] & (rocks[rn][-2] >> rx):
        return True
    return False


def sim(moves, nrocks):
    space = [0b100000001 for _ in range(4)] + [0b111111111]
    rn = 0  # rock num
    rx, ry = 2, 0  # rock position
    stopped = 0

    for m in cycle(moves):
        # move sideways if possible
        rx += side_coll(space, rn, rx, ry, m == "<")
        draw(space, rn, rx, ry)

        if not down_coll(space, rn, rx, ry):
            # move down and move on
            ry += 1
            continue
        
        # render in rock
        for j in range(rh[rn]):
            space[ry + j] |= rocks[rn][j] >> rx

        # find top
        for j in range(len(space)):
            if space[j] & 0b011111110:
                break

        # are we there yet?
        stopped += 1
        if stopped == nrocks:
            draw(space, rn, rx, ry)
            return len(space) - 1 - j

        # spawn new rock
        rn, rx, ry = (rn + 1) % 5, 2, 0

        # grow space
        if j >= 4 + rh[rn]:  # enough rows already, place lower
            ry = j - rh[rn] - 3
        else:
            for _ in range(rh[rn] + 3 - j):
                space.insert(0, 0b100000001)

        if RENDER:
            draw(space, rn, rx, ry)
            print(f"rn: {rn}, rx: {rx}, ry: {ry}")
            input()


RENDER = False

# Part 1
sinp = list(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")
h = sim(sinp, 2022)
print("1. sample", h)
assert(sim(sinp, 2022)) == 3068

inp = open("17.txt").read().strip()
h = sim(inp, 2022)
print("1. real", h)
assert(sim(inp, 2022)) == 3055

# Part 2 - will need to find where the cycle is...
# print(sim(simp, 1000000000000)) #
