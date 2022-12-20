#!/usr/bin/env python3

"""
--- Day 20: Grove Positioning System ---
"""


def parse(lines):
    return [int(l) for l in lines]


def mix(nums, cnt=1):
    l = len(nums)
    idxs = [i for i in range(l)]

    for _ in range(cnt):
        for i, num in enumerate(nums):
            if num == 0:
                continue
            i2 = idxs.index(i)
            n = idxs.pop(i2)
            newidx = (i2 + num) % (l - 1)
            idxs.insert(newidx, n)

    return [nums[i] for i in idxs]


def coords(nums):
    l = len(nums)
    zi = nums.index(0)
    return sum(nums[i] for i in ((zi + ts) % l for ts in [1000, 2000, 3000]))


def one(lines):
    nums = parse(lines)
    return coords(mix(nums))


def two(lines):
    key = 811589153
    nums = list(map(lambda x: x * key, parse(lines)))
    return coords(mix(nums, 10))


sinp = """1
2
-3
3
-2
0
4""".split(
    "\n"
)

inp = open("20.txt").read().strip().split("\n")

print("1-sample:", one(sinp))  # 3
print("1-real:", one(inp))  # 3473

print("2-sample:", two(sinp))  # 1623178306
print("2-real:", two(inp))  # 7496649006261
