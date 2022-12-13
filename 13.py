#!/usr/bin/env python3

"""
--- Day 13: Distress Signal ---

"""


def parse(inp):
    return [[eval(p) for p in pkt.split()] for pkt in inp.strip().split("\n\n")]


def check_pktr(le, re):
    print(f"{le} vs {re}")
    if type(le) == int and type(re) == int:
        if le < re:
            return True
        elif le > re:
            return False
        else:
            return None
    elif type(le) == list and type(re) == list:
        for i in range(max(len(le), len(re))):
            if i >= len(re):
                print("exhausted right")
                return False
            if i >= len(le):
                print("exhausted left")
                return True
            o = check_pktr(le[i], re[i])
            if o is None:
                continue
            else:
                return o
        return True
    elif type(le) == int:
        return check_pktr([le], re)
    elif type(re) == int:
        return check_pktr(le, [re])


def check_pkts(pkts):
    ord_idxs = []
    for i in range(len(pkts)):
        # for i in range(2):
        ordered = check_pktr(pkts[i][0], pkts[i][1])
        print(f"{i+1} is ordered? {ordered}")
        if ordered:
            ord_idxs.append(i + 1)
    return sum(ord_idxs)


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

inp = open("13.txt").read()

# part 1
pkts = parse(sinp)
print(check_pkts(pkts))  # 13

pkts = parse(inp)
print(check_pkts(pkts))  # 6623
