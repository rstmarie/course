# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:53:46 2019

@author: RSM
"""

d={'c':22,'b':1,'a':10}
t=list(d.items())
print(t)

t.sort()
print(t)

for key, val in list(d.items()):
    print(key,val)

p=list()
for key, val in d.items():
    p.append((val, key))
print(p)

p.sort(reverse=True)
print(p)
    