#!/usr/bin/env python3

"""

"""
from functools import cache


RENDER = False


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dc = [">", "v", "<", "^"]
bliz = None
sx, sy = 0, 0


def pboard(stat, x, y, t):
    if RENDER:
        print("board at time ", t, "x,y: ", x, y)
        print("#" * (sx + 2))
        for j in range(sy):
            l = [stat[(i, j)] if (i, j) in stat else "E" if (i, j) == (x, y) else "." for i in range(sx)]
            print("#" + "".join([str(len(c)) if len(c) > 1 else c[0] for c in l]) + "#")
        print("#" * (sx + 2))
        print()
        input()


def parse(inp):
    global bliz, sx, sy
    inp = inp.split("\n")
    # (x,y): [] list of blizzards in each coord
    bliz = {
        (x - 1, y - 1): [c]
        for y, l in enumerate(inp)
        for x, c in enumerate(l)
        if c in dc
    }
    sx = len(inp[0]) - 2
    sy = len(inp) - 2


@cache
def bliz_t(t):
    if t == 0:
        return bliz
    prior = bliz_t(t - 1)
    blizt = {}
    for (x, y), ch in prior.items():
        for c in ch:
            x2, y2 = bnabe(x, y, dirs[dc.index(c)])
            if (x2, y2) in blizt:
                blizt[(x2, y2)].append(c)
            else:
                blizt[(x2, y2)] = [c]
    return blizt


def bnabe(x, y, d):
    x2 = (x + d[0]) % sx
    y2 = (y + d[1]) % sy
    return x2, y2


def enabe(x, y, d):
    x2 = x + d[0]
    y2 = y + d[1]
    if 0 <= x2 < sx and 0 <= y2 < sy:
        return x2, y2
    return False


@cache
def enabes(x, y):
    return list(filter(lambda x: x, [enabe(x, y, d) for d in dirs]))


def sim(s, e, t):
    q = []
    vis = set()

    while True:
        while not q:
            # wait for entry
            t += 1
            if s not in bliz_t(t):
                q.append((s[0], s[1], t))

        x, y, t = q.pop(0)
        if (x, y, t) in vis:
            continue
        vis.add((x, y, t))

        if (x, y) == e:
            print("got to end", x, y, e, t+1)
            return t + 1

        blizt = bliz_t(t)
        pboard(blizt, x, y, t)

        # find possible moves
        blizt = bliz_t(t + 1)
        poss = enabes(x, y) + ([] if (x, y) == s else [(x, y)])
        for (nx, ny) in poss:
            if (nx, ny) not in blizt:
                q.append((nx, ny, t + 1))


def doit(inp):
    parse(inp)
    s = (0, 0)
    e = (sx - 1, sy - 1)  # 1 step before
    t1 = sim(s, e, 0)
    t2 = sim(e, s, t1)
    t3 = sim(s, e, t2)
    return t1, t3


sinp = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""

sinp2 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

inp = open("24.txt").read().strip()

# print("sample 1:", doit(sinp))  # 10
#print("sample 2:", doit(sinp2))  # 18, 54
print("real:", doit(inp))  # 290, 842
