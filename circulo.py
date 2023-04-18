# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 06:42:27 2023

@author: Andres Florez
"""

# Programa que calcula perímetro y área de un círculo
from math import pi
r = float(input('Introduce el radio del círculo: ')) 
per = 2*pi*r
area = pi*r**2 
print('Perímetro =', per)
print('Área =', area)