# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:44:22 2023

@author: Andres Florez
"""

from math import log10
def ganancia_dB(x, y=100): 
    """
    Calcula ganancia en dB: 20log(y/x)
    """
    return 20*log10(y/x)
Vi = 10
print('Ganancia =', ganancia_dB(Vi),'dB')
print('Ganancia =', ganancia_dB(Vi+5, 50),'dB')