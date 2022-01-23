# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:26:23 2021

@author: 0526p
"""

arr = [[-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0, 0, 8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

add_list = []
i = len(arr)-1
j = len(arr[0])-1
k = 0
while k <= i-2:
    l = 0
    while l <= j-2:
        sum_new_list_elements = 0
        new_list = []
        r = k
        s = l
        for m in range(k, r+3):
            for n in range(l, s+3):
                if m == r+1 and n == s+1:
                    new_list.append(arr[m][n])
                elif m == r+1 and (n==s or n == s+2):
                    new_list.append(0)
                else:
                    new_list.append(arr[m][n])
        for o in new_list:
            sum_new_list_elements = sum_new_list_elements + o
        add_list.append(sum_new_list_elements)
        l = l+1
    k = k+1
print(max(add_list))
