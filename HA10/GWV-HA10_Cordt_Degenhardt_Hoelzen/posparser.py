#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import sys

words = []
tags = []
transitionCounts = {}
transitionProbs = {}
emissionCounts = {}
emissionProbs = {}

'''

+---------+    +---------+    +---------+
|  tag0   |--->|  tag1   |--->|  tag2   |--->...
+---------+    +---------+    +---------+
     |              |              |    
     v              v              v    
+---------+    +---------+    +---------+
|  word0  |    |  word1  |    |  word2  |
+---------+    +---------+    +---------+

@words
    Liste aller eingelesenen Wörter
@tags
    Liste aller eingelesenen Tags
@transitionCounts
    Häufigkeit der Transitionen von 'tag_k-1' zu 'tag_k'
    -> Abhängigkeit nur vom vorherigen Tag (im Code 'prevTag')
    Struktur: {tag0: {tag1: 1}, tag1: {tag2: 1}, ...}
@transitionProbs
    Wahrscheinlichkeit der Transitionen von 'tag_k-1' zu 'tag_k'
    umgerechnet von @transitionCounts
    Struktur: {tag0: {tag1: 1.0}, tag1: {tag2: 1.0}, ...}
@emissionCounts
    Häufigkeit der Emission von 'word_k' von 'tag_k'
    Struktur: {tag0: {word0: 1}, tag1: {word1: 1}, ...}
@emissionProbs
    Wahrscheinlichkeit der Emission von 'word_k' von 'tag_k'
    umgerechnet von @emissionCounts
    Struktur: {tag0: {word0: 1.0}, tag1: {word1: 1.0}, ...}

'''

def parse_file(fname):
    '''
    Parsed eine Datei des Formats "word\ttag\n" in die oben definierten Variablen
    '''
    global transitionCounts, transitionProbs, emissionCounts, emissionProbs
    with open(fname, "r") as f:
        lines = f.readlines()
    
    #progress bar
    prog_len = len(lines)
    sys.stdout.write("parsing [%s]" % (" " * 26))
    sys.stdout.flush()
    sys.stdout.write("\b" * 27)

    prevTag = '$.'
    c = 0
    for l in lines:
        #progress bar
        if c == 0:
            sys.stdout.write("#")
            sys.stdout.flush()
        c = (c + 1) % (prog_len / 25)
    
        prevTag = parse_line(l, prevTag)

    sys.stdout.write("\n")

    print "calculating probabilities..."
    transitionProbs = counts_to_probs(transitionCounts)
    emissionProbs = counts_to_probs(emissionCounts)

def parse_line(line, prevTag):
    if line != '\n':
        word, tag = line.strip().split("\t")
        add_word(word, tag, prevTag)
        return tag

def add_word(word, tag, prevTag):
    global words, tags, transitionCounts, emissionCounts
    if words.count(word) == 0:
        words += [word]
    if tags.count(tag) == 0:
        tags += [tag]

    if prevTag not in transitionCounts:
        transitionCounts[prevTag] = {tag : 1}
    elif tag not in transitionCounts[prevTag]:
        transitionCounts[prevTag][tag] = 1
    else:
        transitionCounts[prevTag][tag] += 1

    if tag not in emissionCounts:
        emissionCounts[tag] = {word : 1}
    elif word not in emissionCounts[tag]:
        emissionCounts[tag][word] = 1
    else:
        emissionCounts[tag][word] += 1

def counts_to_probs(counts):
    probs = copy.deepcopy(counts)
    for prevTag, tags in probs.items():
        count = 0
        for tag, tagCount in tags.items():
            count += tagCount
        for tag, tagCount in tags.items():
            probs[prevTag][tag] = float(tagCount) / count
    return probs
