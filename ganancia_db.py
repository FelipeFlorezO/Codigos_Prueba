# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:01:13 2023

@author: Andres Florez
"""

from math import log10
def ganancia_dB(x,y):
    """
    CALCULA GANANCIA EN dB: 20 log(y/x)
    """
    gain = y/x
    dB = 20*log10(gain)
    return dB

Vi = 10
Vo = 1000
GdB = ganancia_dB(Vi,Vo)
print('Ganancia = ', GdB, 'dB')