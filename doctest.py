# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:25:42 2023

@author: Andres Florez
"""

from math import log10

def ganancia_dB(x, y):
    """Calcula ganancia en dB: 20log(y/x)
    >>> ganancia_dB(1,1000) 
    60.0
    >>> ganancia_dB(10,1000)
    40.0
    >>> ganancia_dB(1,1) 
    0.0
    >>> ganancia_dB(10,1)
    -20.0 
    """
    return 20*log10(y/x)

import doctest 

doctest.testmod(verbose=True)