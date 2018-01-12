#!/usr/bin/python
# -*- coding: utf-8 -*-
from posparser import *
import sys

def find_tag(word, prevTag):
    '''
    gibt den wahrscheinlichsten Tag für ein gegebenes Wort und den vorhergehenden Tag aus
    '''
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
    print "Bitte mindestens einen Dateinamen als Parameter übergeben!"
    print "Zeilen der Trainingsdaten müssen das Format \"word<tab>tag\" haben."
    exit()

filenames = sys.argv[1:]
for f in filenames:
    parse_file(f)

    prevTag = '$.'
    while True:
        w = raw_input("finde tag für wort (press Enter to exit): ")
        if not w:
            exit()
        prevTag = find_tag(w, prevTag)
        print str(w) + "\t" + str(prevTag)
