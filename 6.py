#!/usr/bin/env python3

"""
--- Day 6: Tuning Trouble ---

"""


def start_of(signal, n=4):
    """
    4 characters in a row that are all different == packet
    14 characters in a row that are all different == message
    """
    for i in range(n, len(signal)):
        if len(set(signal[i - n : i])) == n:
            return i


inp = open("6.txt").read()

print("part 1:")
assert start_of("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert start_of("bvwbjpwwlbgvbhsrlpgdmjqwftvncz") == 5
print(start_of(inp))  # 1175

print("part 2:")
assert start_of("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert start_of("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
print(start_of(inp, 14))  # 3217
