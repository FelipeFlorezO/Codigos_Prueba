# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:35:57 2023

@author: Andres Florez
"""

def paso(h, m, s):
    """Retorna siguiente valor de horas, 
    minutos y segundos de un cronómetro
    Ejemplos:
    >>> paso(0,0,0) 
    (0, 0, 1)
    >>> paso(0,59,59)
    (1, 0, 0)
    >>> paso(23,59,59) 
    (0, 0, 0)
    """
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0 
    return h, m, s

print(paso(0,0,59))
print(paso(0,0,-1))