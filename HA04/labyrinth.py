#!/usr/bin/python
'''
GWV Hausaufgabe 4

Benjamin Cordt
Felix Degenhardt
Paul Hoelzen
'''

import sys
import re

'''
FUNCTIONS
'''
def find(char):
# finde einen Character im eingelesenen
# ASCII-Labyrinth
    regex = r'.*' + str(char) + '.*'
    y = 0
    for row in env:
        mobj = re.match(regex, row)
        if mobj:
            x = row.index(char)
            return [x, y]
        y += 1
    return False

def adj(vis, pos):
# gibt benachbarte, begehbare Felder zurueck
    ret = []
    adj = [[0,-1], [-1,0], [0,1], [1,0]]
    for p in adj:
        x = pos[0]+p[0]
        y = pos[1]+p[1]
        if env[y][x] != 'x' and not (x,y) in vis:
            ret += [[x,y]]
    return ret


def print_vis(vis, env):
    h = len(env)
    w = len(env[0])
    ret = env
    
    for x in range(w):
        for y in range(h):
            if (x,y) in vis:
                if env[y][x] == ' ':
                    c = '.'
                else:
                    c = env[y][x].upper()
                ret[y] = str(env[y][:x]) + c + str(env[y][x+1:])
    return ret

'''
Breadth-First Search
'''
def bfs_add(frontier, path):
# fuege einen Pfad der Frontier hinzu
# Frontier ist eine Queue, also hinten dran
    return frontier + [path]

'''
Depth-First Search
'''
def dfs_add(frontier, path):
# fuege einen Pfad der Frontier hinzu
# Frontier ist ein Stack, also vorne dran
    return [path] + frontier

def start_search(t):
    start = find('s')
    goal = find('g')
    frontier = [[start]]
    visited = {}

    while frontier:
        path = frontier[0]
        del frontier[0]

        visited[(path[-1][0], path[-1][1])] = 1

        if path[-1] == goal:
            print "visited: "
            print '\n'.join(print_vis(visited, env))
            return path
        
        for next_pos in adj(visited, path[-1]):
            if t == "bfs":
                frontier = bfs_add(frontier, path + [next_pos])
            elif t == "dfs":
                frontier = dfs_add(frontier, path + [next_pos])
            else:
                return None

'''
SETUP
'''
if (len(sys.argv) != 2):
    print "Please specify the file to be parsed like:"
    print str(sys.argv[0]) + " filename"
    exit()

with open(sys.argv[1]) as f:
    # Datei zeilenweise in eine Liste einlesen
    env = f.readlines()

# die '\n' character am Ende der Zeilen entfernen
env = [i.strip('\n') for i in env]


'''
MAIN
'''
print '\n'.join(env)
print "BFS: " + str(start_search("bfs"))
#print "DFS: " + str(start_search("dfs"))
