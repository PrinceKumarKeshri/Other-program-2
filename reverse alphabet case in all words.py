# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:45:28 2021

@author: 0526p
"""


    
i  = 'pRinCe KumAr'
l = i.split(' ')
l.reverse()
l = ' '.join(l)
j = []
for i in l:
    if i == i.lower():
        j.append(i.upper())
    elif i == i.upper():
        j.append(i.lower())

j = ''.join(j)
print(j)

