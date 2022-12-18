#!/usr/bin/env python3

"""
--- Day 18: Boiling Boulders ---
"""
import re
import numpy as np

sz = 42

def parse(lines):
    return [tuple(map(int, re.findall(r"\d+", l))) for l in lines]


def place(vox):
    grid = np.zeros((sz, sz, sz), dtype=int)
    for v in vox:
        grid[v] = 1
    return grid


dirs = np.array([[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]])


def faces(grid):
    cnt = 0
    for z in range(sz - 1):
        for y in range(sz - 1):
            for x in range(sz - 1):
                if grid[(x, y, z)] == 1:
                    for d in dirs:
                        c = np.add([x, y, z], d)
                        if grid[tuple(c)] == 0:
                            cnt += 1
    return cnt


def flood(grid, x, y, z):
    """
    Flood fill from outside
    """
    q = [(x, y, z)]
    area = 0

    while len(q) > 0:
        voxc = q.pop(0)
        # out of bounds or visited
        if min(voxc) < 0 or max(voxc) > sz or grid[voxc] == -1:
            continue

        grid[voxc] = -1  # visited

        # count nabe faces,
        # add empty non-visited nabes in bounds
        for d in dirs:
            nc = tuple(np.add(d, voxc))
            if min(nc) >= 0 and max(nc) < sz:
                if grid[nc] == 1:
                    area += 1
                elif grid[nc] == 0:
                    q.append(nc)

    return area


import fill_voids
def area(grid):
    filled = fill_voids.fill(grid)
    return (faces(filled))

def one(inpl):
    vox = parse(inpl)
    grid = place(vox)
    return faces(grid)


def two(inpl):
    vox = parse(inpl)
    grid = place(vox)
    #return flood(grid, 40, 40, 40)
    return area(grid)


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

inp = open("18.txt").read().strip().split("\n")

print("1-sample:", one(sinp))  # 64
print("1-real:", one(inp))  # 4302

print("2-sample:", two(sinp))  # 58
print("2-real:", two(inp))  # 2492, flood finds 2487(!!?)
