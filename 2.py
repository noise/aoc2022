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

outcome_moves = {'A X': 'Z', # rock, lose: scissors
                 'A Y': 'X', # rock, draw: rock
                 'A Z': 'Y', # rock, win: paper
         
                 'B X': 'X', # paper, lose: rock
                 'B Y': 'Y', # paper, draw: paper
                 'B Z': 'Z', # paper, win: scissors
         
                 'C X': 'Y', # scissors, lose: paper
                 'C Y': 'Z', # scissors, draw: scissors
                 'C Z': 'X'} # scissors, win: rock


def score(moves):
    s = 0
    for m in moves:
        #print(m)
        if m == '':
            continue
        s += move_scores[m[2]]
        s += round_scores[m]
    return s

def score2(outcomes):
    s = 0
    for o in outcomes:
        if o == '':
            continue
        move = outcome_moves[o]
        s += move_scores[move]
        s += round_scores[o[0] + ' ' + move]
    return s

# sample
print(score('''A Y
B X
C Z'''.split('\n')))

# real input
inp = open("2.txt").read()
print(score(inp.split('\n')))

# sample
print(score2('''A Y
B X
C Z'''.split('\n')))

# real input
inp = open("2.txt").read()
print(score2(inp.split('\n')))

