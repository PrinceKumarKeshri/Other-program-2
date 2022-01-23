# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 18:52:21 2021

@author: 0526p
"""
a = [1,2,3,4,5]
print('list: ', a)
print('maximum element in list = ', max(a))
i = 0
j = len(a)
print('swaping indexing position:')
reverse_list_1 = [1, 2, 3, 4, 5]
while i < j:
    print('--', i, j)
    temp = reverse_list_1[i]
    reverse_list_1[i] = reverse_list_1[j-1]
    reverse_list_1[j-1] = temp
    i = i+1
    j = j-1
    
print('Method 1...\n', reverse_list_1)

reverse_list_2 = []
for l in a:
    reverse_list_2.insert(0, l)
    
print('Method 2...\n', reverse_list_2)

print('Method 3...\n', a[::-1])
