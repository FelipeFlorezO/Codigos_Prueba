# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:55:46 2023

@author: Andres Florez
"""

from math import *
def funcion2(x,y,z):
    funcion = ((1 + x * (y - 1)/z)/ 0.5 * (x+3) )
    return funcion

x = float(input('inserte un valor para x: '))
y = float(input('inserte un valor para y: '))
z = float(input('inserte un valor para z: '))
print(funcion2(x, y, z))