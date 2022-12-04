#!/usr/bin/env python3

"""
--- Day 4: Camp Cleanup ---

"""


def overlaps(pairs):
    full, part = 0, 0
    for p in pairs:
        p1, p2 = p.split(",")
        pr1 = set(range(int(p1.split("-")[0]), int(p1.split("-")[1]) + 1))
        pr2 = set(range(int(p2.split("-")[0]), int(p2.split("-")[1]) + 1))

        # full overlaps
        if len(pr1.intersection(pr2)) == len(pr1) or len(pr2.intersection(pr1)) == len(
            pr2
        ):
            full += 1

        # any overlap
        if len(pr1.intersection(pr2)) > 0:
            part += 1

    return full, part


sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip().split(
    "\n"
)

inp = open("4.txt").read().strip().split("\n")

print(overlaps(sample))  # 2, 4
print(overlaps(inp))  # 588, 911
