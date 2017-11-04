#!/usr/bin/python
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


if (len(sys.argv) != 2):
    print "Please specify the file to be parsed like:"
    print str(sys.argv[0]) + " filename"
    exit()

with open(sys.argv[1]) as f:
    # Datei zeilenweise in eine Liste einlesen
    env = f.readlines()

# die '\n' character am Ende der Zeilen entfernen
env = [i.strip('\n') for i in env]

s = find('s')
g = find('g')

print "Datei " + sys.argv[1] + " gelesen."
print '\n'.join(env)
print "start: x " + str(s[0]) + ", y " + str(s[1])
print "goal:  x " + str(g[0]) + ", y " + str(g[1])

# Search states koennten visualisiert werden indem besuchte Felder
# in der 'env' Variable mit neuen Chars ersetzt werden.
