# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2!= 0:
            total = total+num   
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7,8,9,10]))

