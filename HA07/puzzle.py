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

def reduce_domains(d):
    for pos in d:
        for word in d[pos]:
            if not chk_constraints(d, word, pos):
                d[pos].remove(word)
    return d

def print_puzzle(p):
    for i in p:
        print str(i) + ": " + str(p[i])

def solve_rec(p):
    if not none_empty(p):
        return False
    #l = [y for x in p.values() for y in x]
    if not [1 for x in p.values() if len(x) != 1]: # and len(l) == len(set(l)):
        return p
    else:
        p1 = p2 = {}
        for pos in p:
            p1[pos] = p[pos][:len(p[pos]) / 2]
            p2[pos] = p[pos][len(p[pos]) / 2:]
        return solve_rec(p1) or solve_rec(p2)

def vis_puzzle(p):
    a = p["A1"][0][0]
    b = p["A1"][0][1]
    c = p["A1"][0][2]
    d = p["A2"][0][0]
    e = p["A2"][0][1]
    f = p["A2"][0][2]
    g = p["A3"][0][0]
    h = p["A3"][0][1]
    i = p["A3"][0][2]

    print "   | D1 | D2 | D3"
    print "---+----+----+---"
    print "A1 | "+str(a)+"  | "+str(b)+"  | "+str(c)+" "
    print "A2 | "+str(d)+"  | "+str(e)+"  | "+str(f)+" "
    print "A3 | "+str(g)+"  | "+str(h)+"  | "+str(i)+" "

print "Domain consistency"
puzzle = reduce_domains(puzzle)
print_puzzle(puzzle)
print

print "Arc consistency"
diff = {}
while not diff == puzzle:
    diff = dict(puzzle)
    puzzle = reduce_domains(puzzle)
print_puzzle(puzzle)
print

sol = solve_rec(puzzle)
print sol
print 
vis_puzzle(sol)
