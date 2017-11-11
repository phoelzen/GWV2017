#!/usr/bin/python
'''
GWV Hausaufgabe 4

Benjamin Cordt
Felix Degenhardt
Paul Hoelzen
'''

import sys
import re

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

def adj(pos):
# gibt benachbarte, begehbare Felder zurueck
    ret = []
    adj = [[0,-1], [-1,0], [0,1], [1,0]]
    for p in adj:
        n = [pos[0]+p[0], pos[1]+p[1]]
        if env[n[0]][n[1]] != 'x':
            ret += [n]
    return ret

'''
Breadth-First Search
'''
def bfs_add(frontier, path):
# fuege einen Pfad der Frontier hinzu
# Frontier ist eine Queue, also hinten dran
    return frontier + [path]

def bfs_start():
# starte breitensuche
    start = find('s')
    goal = find('g')
    frontier = [[start]]

    while frontier:
        path = frontier[0]
        del frontier[0]

        #print "Frontier: " + str(frontier)
        #print "Selected Path: " + str(path)

        if path[-1] == goal:
            return path
        
        for next_pos in adj(path[-1]):
            frontier = bfs_add(frontier, path + [next_pos])

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
print "BFS: " + str(bfs_start())
