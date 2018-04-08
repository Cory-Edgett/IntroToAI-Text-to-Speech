#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:56:27 2018

@author: sanzla_tv
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import re

cmu_dict = open('Dataset_v1/cmudict.dict', "r")

# conv the dict into a string to regex over it
dictString = cmu_dict.read()
# close dictionary
cmu_dict.close()

def wordsToPhonetics(test):
    # parse through text converting to arpabet
    seg_test = test.split(" ")
    # contain content for sentence given to phonetics
    wordsToPhonetic = {}

    
    # For each word in the given sentence find its phonetic spelling
    for word in seg_test:
    
        # word to regex
        wordRex =  '\\n' + word.lower() + '\s(.*)'
        p = re.compile(wordRex)
        # search in dictionary
        matchedObj = re.search(p, dictString)
        if (matchedObj == None):
            break
        # add phonetic to dictionary, with word as key
        wordsToPhonetic[word] = matchedObj.group(1)
    
    # return value
    return wordsToPhonetic

