#!/usr/bin/env /opt/anaconda3/bin/python3


import sys
import re

print(sys.argv[1])
filename = sys.argv[1]

indexlist = []

with open(filename,"r") as fp:
    Lines = fp.readlines()
    for line in Lines:
        indexlist.append(re.split(r"\.",line)[0])

indexset = set(indexlist)
for item in indexset:
    print(item)