# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:12:53 2023

@author: Andres Florez
"""

def f1(x):
    return (x/2 + 1)

def f2(x):
    print(x/2 + 1)
    
print(f1(5))
print(f2(5))

y2 = 4 + f1(5)
y1 = 4 + f2(5)