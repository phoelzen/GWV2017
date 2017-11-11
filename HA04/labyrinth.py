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
def find(env, char):
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

def adj(env, vis, pos):
# gibt benachbarte, begehbare Felder zurueck
    ret = []
    adj = [[0,-1], [-1,0], [0,1], [1,0]]
    for p in adj:
        x = pos[0]+p[0]
        y = pos[1]+p[1]
        if env[y][x] != 'x' and not (x,y) in vis:
            ret += [[x,y]]
    return ret


def print_vis(env, vis):
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

def start_search(lab, t):
# starte die suche im Labyrinth lab vom Suchtyp t
# t: bfs, dfs
    with open(lab) as f:
        # Datei zeilenweise in eine Liste einlesen
        env = f.readlines()
    # die '\n' character am Ende der Zeilen entfernen
    env = [i.strip('\n') for i in env]
    print '\n'.join(env)
    
    start = find(env, 's')
    goal = find(env, 'g')
    frontier = [[start]]
    visited = {}

    while frontier:
        path = frontier[0]
        del frontier[0]

        visited[(path[-1][0], path[-1][1])] = 1

        if path[-1] == goal:
            print "visited: "
            print '\n'.join(print_vis(env, visited))
            return path
        
        for next_pos in adj(env, visited, path[-1]):
            if t == "bfs":
                frontier = bfs_add(frontier, path + [next_pos])
            elif t == "dfs":
                frontier = dfs_add(frontier, path + [next_pos])
            else:
                return None
'''
#############################
'''

if (len(sys.argv) != 2):
    print "Please specify the file to be parsed like:"
    print str(sys.argv[0]) + " filename"
    exit()
filename = sys.argv[1]

print "BFS: "
print start_search(filename, "bfs")
print "DFS: "
print start_search(filename, "dfs")
