# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 00:13:45 2021

@author: 0526p
"""

#l=[3,6,12]
def integer(A, B, C):
    l =[A, B, C]
    n_l = []
    for i in range(1, 10):
        c = 0
        for j in l:
            if j%i == 0:
                c = c+1
                if c == 2:
                    n_l.append(i)
        
    print(n_l)
    print(len(n_l))

integer(5, 12, 20)