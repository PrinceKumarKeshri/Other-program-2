# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:28:49 2021

@author: 0526p
"""

def return_characters():
    ## get the string values from the user
    ## split those values from spaces
    ### !kindly input values seprated with ','
    ### take two empty list
    #### first empty list 'new_list' stores splitting values
    #### second empty list 'alphabet' stores characters of alphabets without repeating any values

    arr = input("Words Enter       : ")
    split_arr = list(arr.split(','))
    new_list = []
    alphabet = []

    ## after splitting iterate all the elements of the new_list
    ## take a 'text' variable store empty string value that reassing the string value after removing ' ' or '"' symbols 
    ### make a nested looping statement
    ### that again iterate the item which we get string value from the first looping statement
    #### check that string is there any ' ' space or '"' symbols, if it is then remove that using 'pass'
    #### else we make a nested if statement for checking that the characters is in present in the alphabet_list
    ##### if characters is already present in the alphabet_list then pass the loop
    ##### else append the value to the alphabet list

    for i in split_arr:
        text = ''
        for j in i:
            if j == ' ':
                pass
            elif j == '''"''':
                pass
            else:
                if j in alphabet:
                    pass
                else:
                    alphabet.append(j)
                text = text+j
        new_list.append(text)

    ## print the values of new_list
    ## print the values of alphabet

    print('Arrays            : ', new_list)
    print('Smallest Charcters: ', alphabet)
  
return_characters()

