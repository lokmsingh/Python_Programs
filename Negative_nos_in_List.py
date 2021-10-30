# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:15:50 2018

@author: Arun
"""

#### Write a Program to receive only the negative numbers from a list

list = [2,46,445,-2,-4,-6,-33]
list2 = []

for num in list:
    
    if num < 0:
       print(num, end = " ")
