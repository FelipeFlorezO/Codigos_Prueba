# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:07:55 2023

@author: Andres Florez
"""

from math import log10
def ganancia_dB(x,y):
    """
    Calcula ganancia en dB: 20log(y/x)
    """
    
    return 20*log10(y/x)

y = 10
x = 1000
print('Ganancia = ', ganancia_dB(y,x), 'dB')