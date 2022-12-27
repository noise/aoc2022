#!/usr/bin/env python3

"""
--- Day 15: Beacon Exclusion Zone ---

"""
from collections import defaultdict
from itertools import pairwise
import os
import numpy as np


def parse(lines):
    sensors = [[int(i) for i in l.split(",")] for l in lines]
    bounds = (
        min([s[0] for s in sensors]),
        min([s[1] for s in sensors]),
        max([s[2] for s in sensors]),
        max([s[3] for s in sensors]),
    )
    return sensors, bounds


def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def spans_for_row(sensors, bounds, row):
    spans = []
    for (sx, sy, bx, by) in sensors:
        d = dist(sx, sy, bx, by)
        if not (sy + d >= row >= sy - d):
            # fully outside our target row
            continue
        l, r = sx - d + abs(row - sy), sx + d - abs(row - sy)
        spans.append((l, r))
    spans = sorted(spans)
    # print(f"spans for row {row}: {spans}")
    return spans


def b_inside_a(a, b):
    return a[0] <= b[0] and a[1] >= b[1]


def a_intersect_b(a, b):
    # assumes sorted
    return b[0] <= a[1]


def merge_spans(spans):
    m = []
    a = spans[0]
    for i in range(1, len(spans) - 1):
        b = spans[i]
        if b_inside_a(a, b):
            # next
            pass
        elif a_intersect_b(a, b):
            a = (a[0], b[1])
        else:
            m.append(a)
            a = b
    m.append(b)
    # print(f"merged: {m}")
    return m


def two(sensors, bounds, maxy):
    """
    narrow rows we care about (at least min/max y bounds)
    for r in rows
      get spans from sensors for row
      merge / intersect spans
      if remaining spans > 1 then gap found
    """
    for row in range(0, maxy + 1):
        spans = spans_for_row(sensors, bounds, row)
        spans = merge_spans(spans)
        if len(spans) > 1:
            # got it
            print("got it", spans, spans[0][1] + 1, row)
            return ((spans[0][1] + 1) * 4000000) + row


sinp = """2, 18,-2, 15
9, 16,10, 16
13, 2,15, 3
12, 14,10, 16
10, 20,10, 16
14, 17,10, 16
8, 7,2, 10
2, 0,2, 10
0, 11,2, 10
20, 14,25, 17
17, 20,21, 22
16, 7,15, 3
14, 3,15, 3
20, 1,15, 3""".strip().split(
    "\n"
)

sensors, bounds = parse(sinp)
print("bounds", bounds)

spans = spans_for_row(sensors, bounds, 10)
spans = spans_for_row(sensors, bounds, 11)
print(two(sensors, bounds, 20))  # 56000011


inp = open("15.txt").read().strip().split("\n")
sensors, bounds = parse(inp)
print("bounds", bounds)  # bounds (3206, 210553, 3998497, 3617758)

print(two(sensors, bounds, 4000001))  # 13134039205729
