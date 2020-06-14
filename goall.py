#!/usr/bin/env python
# First, do some work, to show -- as requested -- that
# the user input doesn't need to come first.

import random 
import bisect
from shutil import move
from os import remove, close

f = open('dict.txt', 'r+')
dict = f.readlines()
words = []
answs = []


for key in dict:
    key_spt = key.split("/")
    words.append(key_spt[0]);
    answs.append(key_spt[1]);
    
f.close()
i = 0
for word in words:
    user_input = raw_input(word + ": ")
    if user_input == "q": break
   
    if user_input!=answs[i]:
        user_input = raw_input(word + ": ")
        if user_input!=answs[i]:
            print("Very bad! " + word + " = " + answs[i])
   
    i+=1
    
