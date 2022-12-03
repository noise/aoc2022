#!/usr/bin/env python3

"""
--- Day 3: Rucksack Reorganization ---
"""


def prio(i):
    return (ord(i) - 96) if ord(i) > ord("Z") else ord(i) - 38


def mixed_up(sacks):
    outliers = []
    for s in sacks:
        c1, c2 = set(s[0 : int(len(s) / 2)]), set(s[int(len(s) / 2) :])
        outliers.append(list(c1.intersection(c2))[0])
    return sum(prio(i) for i in outliers)


def mixed_up_lc(sacks):
    return sum(
        prio(
            list(set(s[0 : int(len(s) / 2)]).intersection(set(s[int(len(s) / 2) :])))[0]
        )
        for s in sacks
    )


def badges(sacks):
    badges = []
    for i in range(0, len(sacks), 3):
        badge = (
            set(sacks[i])
            .intersection(set(sacks[i + 1]))
            .intersection(set(sacks[i + 2]))
        )
        badges.append(list(badge)[0])
    return sum(prio(b) for b in badges)


def badges_lc(sacks):
    return sum(
        prio(
            list(
                set(sacks[i * 3])
                .intersection(set(sacks[i * 3 + 1]))
                .intersection(set(sacks[i * 3 + 2]))
            )[0]
        )
        for i in range(int(len(sacks) / 3))
    )


sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split(
    "\n"
)

inp = open("3.txt").read().strip().split("\n")

print(mixed_up(sample))  # 157
print(mixed_up(inp))  # 7817
print(mixed_up_lc(sample))
print(mixed_up_lc(inp))

print(badges(sample))  # 70
print(badges(inp))  # 2444
print(badges_lc(sample))
print(badges_lc(inp))
