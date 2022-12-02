#!/usr/bin/env python3

"""
--- Day 2: Rock Paper Scissors ---
"""

move_scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

round_scores = {'A X': 3, # rock, rock: draw
                'A Y': 6, # rock, paper: win
                'A Z': 0, # rock, scissors: lose
                
                'B X': 0, # paper, rock: lose
                'B Y': 3, # paper, paper: draw
                'B Z': 6, # paper, scissors: win

                'C X': 6, # scissors, rock: win
                'C Y': 0, # scissors, paper: lose
                'C Z': 3} # scissors, scissors: draw


def score(moves):
    s = 0
    for m in moves:
        print(m)
        if m == '':
            continue
        s += move_scores[m[2]]
        s += round_scores[m]
    return s


# sample
print(score('''A Y
B X
C Z'''.split('\n')))

# real input
inp = open("2.txt").read()
print(score(inp.split('\n')))
