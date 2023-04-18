# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:22:10 2023

@author: Andres Florez
"""

# Halla solución x, de ecuación ax + b = 0
print('Programa que halla el valor de x de la ecuación: ax + b= 0')
a = float(input('a= '))
b = float(input('b= '))
if a != 0:
    x = -b/a
    print('x =', x)
else:
    print('No es posible dividir por cero')