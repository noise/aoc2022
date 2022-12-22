#!/usr/bin/env python3

"""
--- Day 22: Monkey Map ---
"""
import re


RENDER = True


def pboard(board):
    if RENDER:
        print("\n".join(board))


def parse(inp):
    bl, moves = inp.split("\n\n")
    board = bl.split("\n")
    sx, sy = max([len(l) for l in board]), len(board)
    board = [l.ljust(sx, " ") for l in board]  # pad out
    moves = re.findall("\d+|[LR]", moves)
    moves = [int(_) if not _ in "LR" else _ for _ in moves]
    return (board, moves, sx, sy)


def sim(board, moves, sx, sy):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dc = [">", "v", "<", "^"]
    x, y, d = board[0].index("."), 0, 0  # start right

    if RENDER:
        board[y] = board[y][:x] + dc[d] + board[y][x + 1 :]
    for m in moves:
        # print(m)
        if m == "R":
            d = (d + 1) % 4
        elif m == "L":
            d = (d - 1) % 4
        else:
            n = int(m)
            # move until wall, wrapping
            nx, ny = (x + dirs[d][0]) % sx, (y + dirs[d][1]) % sy
            while n > 0:
                # print(f"moving {n}, at {x},{y}, check {nx},{ny}, n: {n}")
                if board[ny][nx] in ["."] + dc:
                    x, y = nx, ny
                    if RENDER:  # paint our path
                        board[y] = board[y][:x] + dc[d] + board[y][x + 1 :]
                    n -= 1
                elif board[ny][nx] == " ":
                    pass
                else:
                    break
                nx, ny = (nx + dirs[d][0]) % sx, (ny + dirs[d][1]) % sy

        # pboard(board)
        # input()
    print(y + 1, x + 1, d)
    return 1000 * (y + 1) + 4 * (x + 1) + d


def one(inp):
    board, moves, sx, sy = parse(inp)
    return sim(board, moves, sx, sy)


sinp = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

# 151 x 200
inp = open("22.txt").read()

print("1-sample:", one(sinp))  # 6032
print("1-real:", one(inp))  # 186128
