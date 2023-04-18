# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:57:28 2023

@author: Andres Florez
"""

# Algoritmo de Euclides en Python
print('Cálculo del MCD de 2 números usando el algoritmo de Euclides') 
a = int(input('Entra un número natural: '))
b = int(input('Entra otro: ')) 
aa, bb = a, b
while a != b:
    if a > b:
        a = a-b 
    else:
        b = b-a
print('El MCD entre',aa,'y',bb, 'es', a)