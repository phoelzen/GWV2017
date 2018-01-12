#!/usr/bin/python
import sys
import re
import copy

'''
Functions
'''
def find(grid):
    for line in grid:
        if '' in line:
            return [line.index(''), grid.index(line)]

def possible_moves(grid):
    x, y = find(grid)
    ret = []
    if y != 0:
        ret += 'u'
    if y != len(grid)-1:
        ret += 'd'
    if x != 0:
        ret += 'l'
    if x != len(grid[0])-1:
        ret += 'r'
    return ret

def move(grid, d):
    ret = copy.deepcopy(grid)
    x, y = find(grid)
    if d == 'u':
            ret[y][x], ret[y-1][x] = ret[y-1][x], ret[y][x]
    elif d == 'd':
            ret[y][x], ret[y+1][x] = ret[y+1][x], ret[y][x]
    elif d == 'l':
            ret[y][x], ret[y][x-1] = ret[y][x-1], ret[y][x]
    elif d == 'r':
            ret[y][x], ret[y][x+1] = ret[y][x+1], ret[y][x]
    return ret

def print_grid(grid):
    for line in grid:
        print ' '.join([x.ljust(3) for x in line])
    print ''

def heuristic(grid):
    '''
    sum of distances between numbers and their correct positions
    '''
    s = 0
    for x, y in [(x, y) for x in range(4) for y in range(4)]:
        try:
            n = int(grid[y][x])
        except ValueError:
            n = 16
        s += abs(y - ((n-1)/4)) + abs(x - ((n-1)%4))
    return s


def f_add(frontier, path):
    return sorted(frontier + [path], key=lambda p: heuristic(p[-1]) + len(p))

def search(grid):
    frontier = [[grid]]

    count = 0
    while frontier:
        count += 1
        path = frontier[0]
        del frontier[0]
        current_grid = path[-1]

        if heuristic(current_grid) == 0:
            print "###### final path START"
            for g in path:
                print_grid(g)
            print "###### final path END"
            print "finished after " + str(count) + " iterations."
            return True

        for m in possible_moves(current_grid):
            next_grid = move(current_grid, m)
            if not next_grid in path:
                frontier = f_add(frontier, path + [next_grid])
                
'''
Main
'''
if len(sys.argv) < 2:
    print "please specify an input puzzle as a textfile."
    exit()

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

grid = [x.strip().split(";") for x in lines]

print "###### initial state"
print_grid(grid)
print "start search..."
search(grid)

'''
interactive mode
'''
#while True:
#    print_grid(grid)
#    if heuristic(grid) == 0:
#        print "You won!"
#        exit()
#    i = raw_input("make a move! [u, d, l, r; Enter to exit]: ")
#    if not i:
#        exit()
#    grid = move(grid, i.strip())
