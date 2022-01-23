# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:37:06 2021

@author: 0526p
"""
import collections

l = [4,5,6,7,8,9,10,1,11,12,3,2,1]
print('list of elements'+' '*31+': ',l)
occur = collections.Counter(l)
maxx = max(l)
z = 0
for i in range(1, maxx+1):
    if i in l:
        if i == maxx:
            miss = maxx + 1
            break
    elif i not in l:
        miss = i
        break
    
for i,j in occur.items():
    if j==1:
        z = z+1
    elif j==2:
        repeat = i
        
if z!= len(occur):
    l.insert(repeat,miss)
    l.remove(repeat)
    print('sum of missing and repeating element'+' '*11+'= ', miss + repeat)
elif z == len(occur):
    miss = None
    repeat = None

print('missing element'+' '*32+'= ', miss, '\nrepeating element' + ' '*30 + '= ', repeat)
print('replace repeating element from missing element = ', l)
