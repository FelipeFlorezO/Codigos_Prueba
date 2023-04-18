# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:54:06 2023

@author: Andres Florez
"""

# Programa que dice si un número es primo o no (for y break)
def es_primo2(n):
    """Dice si un número natural > 1 es primo o no """
    Primo = True
    for d in range(2, n//2+1):
        if n % d == 0: # Se busca algún divisor 
            Primo = False
            break 
    return Primo

x = int(input('Entra número natural mayor que 1: '))

print('Es primo?',es_primo2(x))