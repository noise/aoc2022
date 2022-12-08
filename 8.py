#!/usr/bin/env python3

"""
--- Day 8: Treetop Tree House ---
"""

import os
import time


def transpose(board):
    return list(map(list, zip(*board)))


def parse(inp):
    trees = [[int(i) for i in list(l)] for l in inp]
    return trees


def printvis(vis, trees):
    os.system("clear")
    for i in range(len(vis)):
        print("".join(str(v) for v in vis[i]), "".join(str(v) for v in trees[i]))


def check_vis(trees, vis):
    for r in range(0, len(trees)):
        vis[r][0] = 1
        vis[r][len(trees[r]) - 1] = 1
        h = trees[r][0]
        for c in range(1, len(trees[r])):
            if trees[r][c] > h:
                vis[r][c] = 1
                h = trees[r][c]

        h = trees[r][len(trees[r]) - 1]
        for c in range(len(trees[r]) - 2, 0, -1):
            if trees[r][c] > h:
                vis[r][c] = 1
                h = trees[r][c]
    return vis


def west(trees, r, c):
    s = 0
    for i in range(c - 1, -1, -1):
        s += 1
        if trees[r][i] >= trees[r][c]:
            break
    return s


def east(trees, r, c):
    s = 0
    for i in range(c + 1, len(trees[r])):
        s += 1
        if trees[r][i] >= trees[r][c]:
            break
    return s


def north(trees, r, c):
    s = 0
    for i in range(r - 1, -1, -1):
        s += 1
        if trees[i][c] >= trees[r][c]:
            break
    return s


def south(trees, r, c):
    s = 0
    for i in range(r + 1, len(trees)):
        s += 1
        if trees[i][c] >= trees[r][c]:
            break
    return s


def check_scenic(trees, scenic):
    for r in range(0, len(trees)):
        h = trees[r][0]
        for c in range(1, len(trees[r])):
            w = west(trees, r, c)
            e = east(trees, r, c)
            n = north(trees, r, c)
            s = south(trees, r, c)
            # print(r,c, ': ', n,w,e,s)
            scenic[r][c] = w * e * n * s
    return scenic


def calc_vis(trees):
    vis = [[0 for _ in range(len(trees[0]))] for _ in range(len(trees))]
    vis = check_vis(trees, vis)
    vis = transpose(check_vis(transpose(trees), transpose(vis)))
    # printvis(vis, trees)
    print(sum([sum(i) for i in vis]))


def calc_scenic(trees):
    scenic = [[0 for _ in range(len(trees[0]))] for _ in range(len(trees))]
    scenic = check_scenic(trees, scenic)
    # printvis(scenic, trees)
    print(max([max(i) for i in scenic]))


inp = """30373
25512
65332
33549
35390""".split(
    "\n"
)

trees = parse(inp)
calc_vis(trees)  # 21
calc_scenic(trees)  # 8

inp = open("8.txt").read().strip().split("\n")
trees = parse(inp)
calc_vis(trees)  # 1695
calc_scenic(trees)  # 287040
