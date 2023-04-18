# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:28:09 2023

@author: Andres Florez
"""

def SumaN(n):
    """Calcula la suma de números naturales del 1 al n dado
    >>> SumaN(20) 
    210
    >>> SumaN(10)
    55
    >>> SumaN(100) 
    5050
    """
    i = 1
    suma = 0 
    while i <= n:
        suma = suma + i 
        i = i + 1
    return suma

n = int(input('escriba un numero'))
print(SumaN(n))