# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:29:26 2023

@author: Andres Florez
"""

def factorial_iter(n): 
    result = 1
    for i in range(2, n+1):
        result *= i 
    return result

n = int(input('ingrese un numero'))
print(factorial_iter(n))