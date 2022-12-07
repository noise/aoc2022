#!/usr/bin/env python3

"""
--- Day 7: No Space Left On Device ---
"""


def pwd(cwd):
    return "/".join(cwd)


def parse(inp):
    # dirty hack to walk back up at the end
    for i in range(10):
        inp.append("$ cd ..")

    dir_sizes = {}
    cwd = []
    for l in inp:
        if l == "$ cd ..":
            if len(cwd) == 1:
                continue
            last_size = dir_sizes[pwd(cwd)]
            cwd.pop()
            dir_sizes[pwd(cwd)] += last_size
        elif l.startswith("$ cd "):
            cwd.append(l[5:])
            assert pwd(cwd) not in dir_sizes
            if pwd(cwd) not in dir_sizes:
                dir_sizes[pwd(cwd)] = 0
        elif l == "$ ls":
            pass
        elif l.startswith("dir"):
            pass
        else:  # assume file
            s = int(l.split(" ")[0])
            dir_sizes[pwd(cwd)] += s
    return dir_sizes


def small_dirs(dir_sizes):
    return sum(v for v in dir_sizes.values() if v <= 100000)


def to_delete(dirs):
    AVAIL = 70000000
    NEED = 30000000
    to_del = NEED - (AVAIL - dirs["/"])
    print("to_del", to_del)
    ss = sorted(dirs.items(), key=lambda x: x[1])
    return list(filter(lambda x: x[1] > to_del, ss))[0]


inp = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split(
    "\n"
)

dirs = parse(inp)
print(small_dirs(dirs))  # 95437
print(to_delete(dirs))  # ('/d', 24933642)

inp = open("7.txt").read().strip().split("\n")
dirs = parse(inp)
print(small_dirs(dirs))  # 1390824
print(to_delete(dirs))  # ('/cvt/djb/hvfvt', 7490863)
