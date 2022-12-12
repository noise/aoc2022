#!/usr/bin/env python3

"""
--- Day 12: Hill Climbing Algorithm ---
"""

from collections import defaultdict

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def parse(inp):
    lines = inp.strip().split("\n")
    grid = [list(l) for l in lines]

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "S":
                s = (j, i)
                grid[j][i] = "a"
            if grid[j][i] == "E":
                e = (j, i)
                grid[j][i] = "z"
    return grid, s, e


def climb(grid, e, s, two=False):
    vis = defaultdict(lambda: False)
    Q = [(s, 0)]
    vis[s] = True

    while len(Q) > 0:
        c, dist = Q.pop(0)
        cl = grid[c[0]][c[1]]

        if c == e or (two and cl == "a"):
            return dist

        for d in dirs:
            tc = (c[0] + d[0], c[1] + d[1])

            # check boundaries
            if (tc[0] < 0 or tc[0] > len(grid) - 1 or tc[1] < 0 or tc[1] > len(grid[0]) - 1):
                continue

            # uphill 1 or downhill any, but we are going backward
            tl = grid[c[0] + d[0]][c[1] + d[1]]
            if not vis[tc] and ord(cl) - ord(tl) <= 1:
                Q.append((tc, dist + 1))
                vis[tc] = True


sinp = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

inp = open("12.txt").read()

# part 1
grid, start, end = parse(sinp)
print(climb(grid, start, end, False))  # 31
grid, start, end = parse(inp)
print(climb(grid, start, end, False))  # 380

# part 2
grid, start, end = parse(sinp)
print(climb(grid, start, end, True))  # 29
grid, start, end = parse(inp)
print(climb(grid, start, end, True))  # 375
