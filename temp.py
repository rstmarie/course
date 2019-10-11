# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

txt='but soft what light in yonder window breaks'
words= txt.split()
t=list()
for word in words:
    t.append((len(word),word))
print(t)
t.sort() #replace with t.sort(reverse=True) for decreasing order

res=list()
for leng, word in t:
    res.append(word)
    
print(res)
#prints...['in', 'but', 'soft', 'what', 'light', 'breaks', 'window', 'yonder']