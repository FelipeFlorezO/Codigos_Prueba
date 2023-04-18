# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:30:03 2023

@author: Andres Florez
"""

# Programa que dice si un número es primo o no
n = int(input('Entra un número natural mayor que 1: '))
d = 2
un_divisor = False # Si hay un divisor el número NO es primo 
while d < n and not un_divisor:
    if n % d == 0: # Se busca algún divisor
        un_divisor = True
    d = d + 1
print('Es primo? ',not un_divisor)