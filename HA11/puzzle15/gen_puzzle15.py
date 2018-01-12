#!/usr/bin/python
import sys
import random

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
    x, y = find(grid)
    if d == 'u':
            grid[y][x], grid[y-1][x] = grid[y-1][x], grid[y][x]
    elif d == 'd':
            grid[y][x], grid[y+1][x] = grid[y+1][x], grid[y][x]
    elif d == 'l':
            grid[y][x], grid[y][x-1] = grid[y][x-1], grid[y][x]
    elif d == 'r':
            grid[y][x], grid[y][x+1] = grid[y][x+1], grid[y][x]
    return grid

def print_grid(grid):
    for line in grid:
        print ';'.join(line)

'''
Main
'''
if len(sys.argv) < 2:
    print "please pass the number of turns to scramble the puzzle as an argument."
    exit()

grid = [['1', '2', '3', '4'], ['5', '6', '7', '8'],\
        ['9', '10', '11', '12'], ['13', '14', '15', '']]

last = ''
for _ in range(int(sys.argv[1])):
    m = random.choice(possible_moves(grid))
    if not m == last:
        grid = move(grid, m)
        last = m

print_grid(grid)
