# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:15:55 2023

@author: Andres Florez
"""

from math import pi, atan
def arctan(x, epsilon=1e-9):
    """
    >>> arctan(1) 
    45.0
    >>> round(atan(1)*180/pi, 2)
    45.0
    """
    n=1
    signo = 1 
    term = x 
    suma = x
    while abs(term)>epsilon and n<10000: 
        n += 2
        signo=-signo
        term = signo*x**n/n
        suma += term
    return round(suma*180/pi,2)
