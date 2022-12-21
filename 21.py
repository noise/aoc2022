#!/usr/bin/env python3

"""
--- Day 21: Monkey Math ---
"""


def parse(lines):
    mnums = {}
    mops = []
    for l in lines:
        name, op = l.split(": ")
        try:
            op = int(op)
            mnums[name] = op
        except:
            m1, op, m2 = op.split(" ")
            mops.append((name, m1, op, m2))
    return mnums, mops


def sim(mnums, mops):
    while len(mops) > 0:
        m0, m1, op, m2 = mops.pop(0)
        if m1 in mnums and m2 in mnums:
            if op == "+":
                v = mnums[m1] + mnums[m2]
            elif op == "-":
                v = mnums[m1] - mnums[m2]
            elif op == "*":
                v = mnums[m1] * mnums[m2]
            elif op == "/":
                v = mnums[m1] / mnums[m2]
            else:
                raise
            mnums[m0] = v
        else:
            mops.append((m0, m1, op, m2))
    return mnums["root"]


def one(lines):
    mnums, mops = parse(lines)
    return sim(mnums, mops)


sinp = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split(
    "\n"
)

inp = open("21.txt").read().strip().split("\n")

print("1-sample:", one(sinp))  # 152
print("1-real:", one(inp))  # 49288254556480

# print("2-sample:", two(sinp))  # 301
# print("2-real:", two(inp))  #
