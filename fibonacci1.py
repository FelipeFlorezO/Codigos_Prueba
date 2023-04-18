# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:52:38 2023

@author: Andres Florez
"""

def fiboI(k):
    if k == 1 or k == 2: 
        result = 1
    else:
        a, b = 1, 1
        for i in range(k-1):
            a, b = b, a+b
        result = a 
    return result

print(fiboI(30))