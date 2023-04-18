# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:32:18 2023

@author: Andres Florez
"""

def factorial_r(n):
    if n == 0:
        return 1 
    else:
        return n*factorial_r(n-1)
    
n = int(input('ingrese un numero: '))
print(factorial_r(n))