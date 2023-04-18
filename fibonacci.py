# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:49:34 2023

@author: Andres Florez
"""

def fibo(k):
    if k == 1 or k == 2: 
        result = 1
    else:
        result = fibo(k-1) + fibo(k-2) 
    return result

print(fibo(8))