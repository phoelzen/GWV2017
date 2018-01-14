#!/usr/bin/python
import sys
import itertools as it
import copy

def col(words, c):
    '''
    outputs a list of every 'c'th character from the right of every word in 'words'
    convenience function for aligning characters
    '''
    c += 1
    ret = []
    for w in words:
        if c <= len(w):
            ret.append(w[-c])
        else:
            ret.append('_')
    return ret

def check_unary(var, num, words):
    # leading zero
    if num == 0 and var in [x[0] for x in words]:
        return False
    else:
        return True

def check_sum(var, num, words, max_len, domains):
    doms = copy.deepcopy(domains)
    doms[var] = [num]

    carriers = [0 for _ in range(max_len)]

    #for i in range(max_len):
    for c in [col(words, i) for i in range(max_len)]:
        if var in c:
            a_col = c[:-1]
            s_col = c[-1]
            a_sum = set([sum(v) for v in it.product(*[doms[x] for x in a_col])])

            return any([n%10 in doms[s_col] for n in a_sum])
            #return bool(a_sum.intersection(doms[s_col]))
                
'''
MAIN
'''
if len(sys.argv) < 3:
    print "please specify at least two words for the puzzle"
    exit()

words = sys.argv[1:]
variables = list(set(''.join(words)))
domains = {'_': [0]}
for v in variables:
    domains[v] = range(10)
max_len = max([len(x) for x in words])

#domain consistency
for v in variables:
    for n in range(10):
        if not check_unary(v, n, words):
            domains[v].remove(n)

print "a"
for i in domains['a']:
    print str(i) + " " + str(check_sum('a', i, words, max_len, domains))

print "b"
for i in domains['b']:
    print str(i) + " " + str(check_sum('b', i, words, max_len, domains))
