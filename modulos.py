# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 05:32:49 2023

@author: Andres Florez
"""

from random import randint 
n = randint(10, 100)/3.2567 
print(n, round(n,2))


from math import sqrt, log10 
x= input(('Inserte un valor para x: '))
x = sqrt(10)
dB = 20*log10(x/2)
print(dB)