#!/usr/bin/env python3

"""
--- Day 13: Distress Signal ---

"""
from functools import cmp_to_key


def parse(inp):
    return [[eval(p) for p in pkt.split()] for pkt in inp.strip().split("\n\n")]


def parse2(inp):
    return [eval(p) for p in inp.strip().split("\n") if p != ""]


def check_pktr(le, re):
    # print(f"{le} vs {re}")
    if le == re:
        return 0

    if type(le) == int and type(re) == int:
        if le < re:
            return -1
        elif le > re:
            return 1
    elif type(le) == list and type(re) == list:
        for i in range(max(len(le), len(re))):
            if i >= len(re):
                return 1
            if i >= len(le):
                return -1
            o = check_pktr(le[i], re[i])
            if o == 0:
                continue
            else:
                return o
        return 1
    elif type(le) == int:
        return check_pktr([le], re)
    elif type(re) == int:
        return check_pktr(le, [re])


def check_pkts(pkts):
    ord_idxs = []
    for i in range(len(pkts)):
        ordered = check_pktr(pkts[i][0], pkts[i][1])
        # print(f"{i+1} is ordered? {ordered}")
        if ordered == -1:
            ord_idxs.append(i + 1)
    return sum(ord_idxs)


def two(pkts):
    d1 = [[2]]
    d2 = [[6]]
    pkts.append(d1)
    pkts.append(d2)
    spkts = sorted(pkts, key=cmp_to_key(check_pktr))
    return (spkts.index(d1) + 1) * (spkts.index(d2) + 1)


sinp = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


# sample part 1
pkts = parse(sinp)
print(check_pkts(pkts))  # 13
# part 2
pkts = parse2(sinp)
print(two(pkts))  # 140

# real part 1
inp = open("13.txt").read()
pkts = parse(inp)
print(check_pkts(pkts))  # 6623

# part 2
inp = open("13.txt").read()
pkts = parse2(inp)
print(two(pkts))  # 23049
