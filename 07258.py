#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:09:45 2018

@author: porames
"""
import math
from functools import reduce
f = open("data.txt")
db = {}
def sd(li):
    mean = float(sum(li)) / len(li)
    sd =  math.sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, li))) / (len(li)-1))  
    tore = str(round(mean,2))+" "+str(round(sd,2))
    return (tore)
    #เครดิต https://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
s = 0.0
for line in f:
    line = line.strip().split(':')
    if line[2] in db:
        db[line[2]].append(float(line[3]))
    else:
        db[line[2]] = [float(line[3])]
f.close()
f = open("data.out","w")
for room in db:
    f.write(room+" "+sd(db[room])+"\n")
    print(room+" "+sd(db[room]))
f.close()