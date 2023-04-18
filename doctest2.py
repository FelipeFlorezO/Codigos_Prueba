# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:29:46 2023

@author: Andres Florez
"""

def suma(a, b):
    """Realiza la suma de dos números. 
    Ejemplos:
    >>> suma(1, 2)
    3
    >>> suma(10, 10)
    20 
    """
    return a-b
res = suma(3, 4) 

print(res) 

import doctest
doctest.testmod()