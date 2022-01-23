# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

l = [10,2,3,4,5,6,7,8,9,10]
l.sort()
l_sort=l
j = 0
print('j', 'l', 'i')
print()
for i in range(1, len(l_sort)+1):
    if l_sort[j] == i:
        print(j,l_sort[j], i)
        pass
    elif l_sort[j] != i:
        print(j, l_sort[j], i)
        #if l_sort[j]>l_sort[j-1]:
         #   l_sort.insert(j, i)
        if l_sort[j]>i:
            #if j+1 <len(l_sort):
            #if l_sort[j]==l_sort[j+1]:
            l_sort.insert(j, i)
            l.pop(j+1)
        elif l_sort[j]<i:
            l_sort.insert(j, i)
            l.pop(j+1)
    j = j+1
print(l_sort)