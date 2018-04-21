#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:56:27 2018

@author: sanzla_tv
"""

from translator import wordsToPhonetics
from Speak import sayThis

print("Say \"stop\" to exit")
print ("What can I say for you?")

while(1):
    ans = input(">>")
    if ans == "stop":
        break
    dict = wordsToPhonetics(ans)

    combPhonetics = []
    for word, phonetic in dict.items():
        splitted = phonetic.split(" ")
        for ph in splitted:
            combPhonetics.append(ph)

        combPhonetics.append("SPC")

    sayThis(combPhonetics)

