#!/usr/bin/env python3

"""
Top caloric elf and sum of top 3
"""

def elf_cals():
    inp = open("1.txt").read()
    return sorted([sum([int(n) for n in l.strip().split('\n')]) for l in inp.split('\n\n')])


cals = elf_cals()
print(cals[-3:], sum(cals[-3:]))
