# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:03:36 2023

@author: Andres Florez
"""

import math as ma
def funcion3(x,y):
    funcion = 1 - (1)/ma.sqrt((x-y)**2 + (y-x)**3)
    return funcion

x = float(input('inserte el valor de x: '))
y = float(input('inserte el valor de y: '))
print(funcion3(x, y))