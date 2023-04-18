# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:29:23 2023

@author: Andres Florez
"""
import math as ma
def funcion1(x,a):
    funcion = ma.sqrt(1 - (1+x)/2*a)
    return funcion

x = float(input('inserte un valor para x '))
a = float(input('inserte un valor para a '))
print(funcion1(x,a))