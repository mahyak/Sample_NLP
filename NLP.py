#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:13:27 2020

@author: mahya
"""

from nltk.corpus import wordnet

poses = {'n': 'noun', 'v': 'vers', 's': 'adj(s)', 'a':'adj', 'r': 'adv'}

for synset in wordnet.synsets('good'):
    print("{}: {}".format(poses[synset.pos()], 
                          ", ".join([l.name() for l in synset.lemmas()])))