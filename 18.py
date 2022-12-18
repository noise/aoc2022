#!/usr/bin/env python3

"""
--- Day 18: Boiling Boulders ---
"""
import re
import numpy as np

s = 30


def parse(lines):
    return [tuple(map(int, re.findall("\d+", l))) for l in lines]


def place(vox):
    grid = np.zeros((s, s, s))
    for v in vox:
        print(v)
        grid[v] = 1
    return grid


dirs = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]


def faces(grid):
    cnt = 0
    for z in range(s - 1):
        for y in range(s - 1):
            for x in range(s - 1):
                if grid[(x, y, z)] == 1:
                    for d in dirs:
                        c = np.add([x, y, z], d)
                        if grid[tuple(c)] == 0:
                            cnt += 1
    return cnt


sinp = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".split(
    "\n"
)


vox = parse(sinp)
grid = place(vox)
fcnt = faces(grid)
print("1-sample:", fcnt)  # 64


inp = open("18.txt").read().strip().split("\n")
vox = parse(inp)
grid = place(vox)
fcnt = faces(grid)
print("1. real", fcnt)  # 4302
