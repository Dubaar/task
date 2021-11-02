# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:43:03 2021

@author: BinuShaakir
"""
#import oving_1_rein_tekst(1).txt

with open("oving_1_rein_tekst (1).txt","r", encoding="utf8") as file:
 
    line_number = 0
    dictionary = dict()
   
    for line in file:
        line_number = line_number + 1
        words = line.split()
        for word in words:
            word=word.lower()
            word=word.strip(',.:;()')
            dictionary[word] = line_number
            
print(dictionary)



