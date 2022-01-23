# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:42:07 2021

@author: 0526p
"""
items = int(input("Enter integer = "))
j = 0
power = []
max_lim = int(items/2)
for i in range(max_lim+1):
    square = 2**i
    power.append(square)
if items in power:
    print(items)
else:
    for i in power:
        if i<items:
            j = j+1
        elif i>items:
            print(power[j-1])
            break
