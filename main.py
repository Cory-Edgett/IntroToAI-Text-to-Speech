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
from translator import wordsToPhonetics

print ("What can I say for you?")

while(1):
    testIn = input(">>")
    if testIn == "-1":
        break
    print(wordsToPhonetics(testIn))
