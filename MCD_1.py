# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:14:51 2023

@author: Andres Florez
"""

# Algoritmo de Euclides en Python 
def mcd(a,b):
    """Algoitmo de Euclides, halla máximo común divisor de a y b
    >>> mcd(8,20)
    4
    >>> mcd(24,17) 
    1
    """
    while a != b:
        if a > b:
            a = a-b 
        else:
            b = b-a
    return a

c = mcd(4,5)
print(c)