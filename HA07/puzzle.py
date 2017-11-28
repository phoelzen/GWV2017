#!/usr/bin/python

wordlist = ["add","and","art","bag","far","ado","any","ash","ban","fat","age","ape","ask","bat","fit","ago","apt","auk","bee","lee","aid","arc","awe","boa","oaf","ail","are","awl","ear","rat","aim","ark","aye","eel","tar","air","arm","bad","eft","tie"]

index = ["A1", "A2", "A3", "D1", "D2", "D3"]
puzzle = {}

for i in index:
    puzzle[i] = wordlist[:]

def none_empty(d):
    for k in d:
        if not d[k]:
            return False
    return True

def chk_idx(word, wi, wlist, wli):
    return word[wi] in [x[wli] for x in wlist]

def chk_constraints(d, word, pos):
    switch = {
        "A1": chk_idx(word, 0, d["D1"], 0) and chk_idx(word, 1, d["D2"], 0) \
                and chk_idx(word, 2, d["D3"], 0),
        "A2": chk_idx(word, 0, d["D1"], 1) and chk_idx(word, 1, d["D2"], 1) \
                and chk_idx(word, 2, d["D3"], 1),
        "A3": chk_idx(word, 0, d["D1"], 2) and chk_idx(word, 1, d["D2"], 2) \
                and chk_idx(word, 2, d["D3"], 2),
        "D1": chk_idx(word, 0, d["A1"], 0) and chk_idx(word, 1, d["A2"], 0) \
                and chk_idx(word, 2, d["A3"], 0),
        "D2": chk_idx(word, 0, d["A1"], 1) and chk_idx(word, 1, d["A2"], 1) \
                and chk_idx(word, 2, d["A3"], 1),
        "D3": chk_idx(word, 0, d["A1"], 2) and chk_idx(word, 1, d["A2"], 2) \
                and chk_idx(word, 2, d["A3"], 2),
    }
    return switch.get(pos, False)

# domain consistency
for pos in puzzle:
    for word in puzzle[pos]:
        if not chk_constraints(puzzle, word, pos):
            puzzle[pos].remove(word)
    print str(pos) + ": " + str(puzzle[pos])
    print 

diff = {}
while not diff == puzzle:
    # arc consistency
    diff = dict(puzzle)
    for pos in puzzle.viewkeys():
        for word in puzzle[pos]:
            if not chk_constraints(puzzle, word, pos):
                puzzle[pos].remove(word)

for k in puzzle:
    print str(k) + str(puzzle[k])
