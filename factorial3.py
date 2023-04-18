# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:46:40 2023

@author: Andres Florez
"""

def factorial_r(n): 
    if n == 0:
        result = 1
    else:
        result = n*factorial_r(n-1) 
    return result

print(factorial_r(5))
