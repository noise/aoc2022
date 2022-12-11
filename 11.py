#!/usr/bin/env python3

"""
--- Day 11: Monkey in the Middle ---
"""
import re

inp = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class Monkey(object):
    def __init__(self, conf, n):
        self._parse(conf, n)
        self.inspected = 0

    def __repr__(self):
        return f"""Monkey({self.num}, {self.items}, {self.exp}, {self.mod}, {self.pos_monkey}, {self.neg_monkey}, ninsp: {self.inspected})\n"""

    def _parse(self, conf, n):
        conf = conf.split("\n")
        self.num = n
        self.items = [int(i) for i in re.findall("(\d+)", conf[1])]
        self.exp = conf[2].split("=")[1]
        self.mod = int(re.findall("\d+", conf[3])[0])

        self.pos_monkey = int(re.findall("\d+", conf[4])[0])
        self.neg_monkey = int(re.findall("\d+", conf[5])[0])


def parse(inp):
    monkeystrs = inp.strip().split("\n\n")
    monkeys = []
    for n in range(len(monkeystrs)):
        monkeys.append(Monkey(monkeystrs[n], n))
    return monkeys


def sim(monkeys, rounds, decay=True):
    # the trick, using modulo arithmetics
    # I clearly missed this day of math class and looked up this part of the solution
    mods = 1
    for m in monkeys:
        mods *= m.mod

    for i in range(1, rounds + 1):
        for m in monkeys:
            while m.items:
                old = m.items.pop(0)

                # inspect
                worry = eval(m.exp)
                m.inspected += 1

                # worry level decay for part 1
                if decay:
                    worry = worry // 3

                # the trick, see above
                worry = worry % mods

                # throw to other monkey, add to end of items
                target = m.pos_monkey if worry % m.mod == 0 else m.neg_monkey
                monkeys[target].items.append(worry)

        if i % 1000 == 0 or i == 20:
            insp = sorted([m.inspected for m in monkeys], reverse=True)
            biz = insp[0] * insp[1]
            print(f"Round {i}: biz: {biz}, {insp}")

    return monkeys, biz


# part 1
monkeys = parse(inp)
print(sim(monkeys, 20))  # 10605
monkeys = parse(open("11.txt").read())
print(sim(monkeys, 20))  # 99852

# part 2
monkeys = parse(inp)
print(sim(monkeys, 10000, False))  # 2713310158
monkeys = parse(open("11.txt").read())
print(sim(monkeys, 10000, False))  # 25935263541
