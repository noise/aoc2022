#!/usr/bin/env python3

"""
--- Day 5: Supply Stacks ---

"""
import re
from parse import parse


def transpose(board):
    return list(map(list, zip(*board)))


def parse_inp(inp):
    crates, moves_str = inp.split("\n\n")

    # crates
    crates = crates.split("\n")
    crates.pop()
    crates = [re.findall("[\[\ ]([A-Z\ ])[\]\ ]\ ?", c) for c in crates]
    crates = transpose(crates)
    # trim the empty tops of stacks
    crates = [[c for c in p if c != " "] for p in crates]
    print(crates)

    # moves
    moves = [
        parse("move {:d} from {:d} to {:d}", m) for m in moves_str.strip().split("\n")
    ]
    return crates, moves


def sim_moves(crates, moves):
    for m in moves:
        n, src, dst = m
        for i in range(n):
            c = crates[src - 1].pop(0)
            crates[dst - 1].insert(0, c)
    return "".join([c[0] for c in crates])


def sim_moves_9001(crates, moves):
    for m in moves:
        n, src, dst = m
        for i in range(n):
            c = crates[src - 1].pop(0)
            crates[dst - 1].insert(i, c)
    return "".join([c[0] for c in crates])


s_inp = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

inp = open("5.txt").read()

# part 1
crates, moves = parse_inp(s_inp)
print(sim_moves(crates, moves))  # CMZ
crates, moves = parse_inp(inp)
print(sim_moves(crates, moves))  # BWNCQRMDB

# part 2
crates, moves = parse_inp(s_inp)
print(sim_moves_9001(crates, moves))  # MCD
crates, moves = parse_inp(inp)
print(sim_moves_9001(crates, moves))  # NHWZCBNBF
