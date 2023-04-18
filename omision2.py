# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:18:55 2023

@author: Andres Florez
"""

def fkey(x, y=1, z=1, w=0):
    return (x + y)*(z + w)
print(fkey(2)) # x=2, y=1, z=1, w=0
print(fkey(2, w = 4)) # x=2, y=1, z=1, w=4
print(fkey(1, z = 2, y = 3)) # x=1, y=3, z=2, w=0