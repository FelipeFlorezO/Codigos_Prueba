# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:29:31 2023

@author: Andres Florez
"""

# Paridad de un número
def paridad(num):
    '''Comprueba si un número es par o impar. Ejemplos:
    >>> paridad(4)
    'par'
    >>> paridad(5) 
    'impar'
    '''
    if num%2 == 0:
        res = "par"
    else: # equivaldría a: if num%2 != 0: 
        res = "impar"

    return res

a = paridad(6)
print(a)