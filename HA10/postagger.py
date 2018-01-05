#!/usr/bin/python
from posparser import *
import sys

def find_tag(word, prevTag):
    ltags = []
    for tag, words in emissionCounts.items():
        for tword, count in words.items():
            if word == tword:
                ltags += [(count, tag)]
    if not ltags:
        return None
    return max(ltags)[1]

#MAIN CODE

if len(sys.argv) < 2:
    print "bitte mindestens einen dateinamen als parameter uebergeben!"
    exit()

filenames = sys.argv[1:]
for f in filenames:
    parse_file(f)

    prevTag = '$.'
    while True:
        w = raw_input("wort fuer das ein tag gefunden werden soll: ")
        if not w:
            exit()
        prevTag = find_tag(w, prevTag)
        print str(w) + "\t" + str(prevTag)
