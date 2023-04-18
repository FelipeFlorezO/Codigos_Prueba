# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:51:30 2023

@author: Andres Florez
"""

# Programa que dice si un número es primo o 

def es_primo(n):
    """Dice si un número natural > 1 es primo o no """
    d = 2
    Primo = True # Si hay un divisor el número NO es primo
    while d < n//2 and Primo:
        if n % d == 0: # Se busca algún divisor 
            Primo = False
        d = d + 1
    return Primo

x = int(input('Entra número natural mayor que 1: ')) 
print('Es primo?',es_primo(x))