# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 06:30:54 2021

@author: 0526p
"""

def minimumBribes(q):
    dummy=[]
    values = []
    i = 1
    count = 0
    total_count = 0
    while True:
        dummy = []
        i =1
        while i!=len(q):
            if q[i-1] > q[i]:
                temp = q[i-1]
                q[i-1] = q[i]
                q[i] = temp
                count = count + 1
                total_count = total_count + 1
                dummy.append(q[i-1])
                dummy.append(q[i])
            else:
                dummy.append(q[i])
                count = 0
            if i+1 == len(q):
                values.append(total_count)
            
            if count > 2:
                values.append('Too chaotic')
                break
            else:
                pass
            i = i+1
        print(q)
        if dummy == q:
            print('equal')
            break
        #if i+1 == len(q):
         #   print(value_assign)
          #  value_assign = total_count
    output = values[-1]
    print(output)


minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])