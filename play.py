#!/usr/bin/env python
# First, do some work, to show -- as requested -- that
# the user input doesn't need to come first.

import random 
import bisect
from shutil import move
from os import remove, close
import sys

name = sys.argv[1]
f = open(name, 'r+')

dict = f.readlines()
words = []
answs = []
weighs = []
guesss = []
wrongs = []

for key in dict:
    key_spt = key.split("/")
    words.append(key_spt[0]);
    answs.append(key_spt[1]);
    guess = key_spt[2]
    guesss.append(int(guess))
    wrong = key_spt[3]
    wrong = wrong[:-1]
    wrongs.append(int(wrong))
    weighs.append(0)
    
f.close()

def calcWeight(weighs):
    sumow = 0
    i=0
    for k in wrongs:
        if(float(wrongs[i])/float(guesss[i])==0): sumow +=0.0001
        else: sumow += float(wrongs[i])/float(guesss[i])
        weighs[i]=sumow
        i+=1

def getItem(weighs):
    score = random.random() * weighs[-1]
    i = bisect.bisect(weighs, score)
    return i 
    
while True:
    calcWeight(weighs)
    i = getItem(weighs)
    user_input = raw_input(words[i] + ": ")
    if user_input == "q": break
    guesss[i] += 1
    if user_input!=answs[i]:
        user_input = raw_input(words[i] + ": ")
        if user_input!=answs[i]:
            print("Very bad! " + words[i] + " = " + answs[i])
            wrongs[i] += 1

f = open(name, 'w')
i = 0  
for key in dict:
    f.write(words[i]+"/"+answs[i]+"/"+str(guesss[i])+"/"+str(wrongs[i])+"\n")
    i+=1
f.close()
    
