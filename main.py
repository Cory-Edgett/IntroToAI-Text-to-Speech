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

test = input("What can I say for you?\n")

cmu_dict = open('Dataset_v1/cmudict.dict', "r")

parsedDict = []
wordsToPhonetic = {}

# parse through text converting to arpabet
seg_test = test.split(" ")

dictString = cmu_dict.read()

for word in seg_test:

    wordRex =  '\\n' + word + '\s(.*)'
    
    p = re.compile(wordRex)
    
    matchedObj = re.search(p, dictString)
    
    wordsToPhonetic[word] = matchedObj.group(1)
    
print(wordsToPhonetic)
    


# close dictionary
cmu_dict.close()
