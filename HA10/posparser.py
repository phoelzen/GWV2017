#!/usr/bin/python
import copy

words = []
tags = []
transitionCounts = {}
transitionProbs = {}
emissionCounts = {}
emissionProbs = {}

def parse_file(fname):
    global words, tags, transitionCounts, transitionProbs, emissionCounts, emissionProbs
    with open(fname, "r") as f:
        lines = f.readlines()
    
    prevTag = '$.'
    for l in lines:
        prevTag = parse_line(l, prevTag)
    transitionProbs = counts_to_probs(transitionCounts)
    emissionProbs = counts_to_probs(emissionCounts)

def add_word(word, tag, prevTag):
    global words, tags, transitionCounts, transitionProbs, emissionCounts, emissionProbs
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

def parse_line(line, prevTag):
    if line != '\n':
        word, tag = line.strip().split("\t")
        add_word(word, tag, prevTag)
        return tag

def counts_to_probs(counts):
    probs = copy.deepcopy(counts)
    for prevTag, tags in probs.items():
        count = 0
        for tag, tagCount in tags.items():
            count += tagCount
        for tag, tagCount in tags.items():
            probs[prevTag][tag] = float(tagCount) / count
    return probs
