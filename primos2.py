# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:32:44 2023

@author: Andres Florez
"""

def es_primo(n):
    """Función que devuelve True o False si n es primo o no
    >>> es_primo(57) 
    False
    >>> es_primo(59)
    True 
    """
    d = 2
    Primo = True # Si hay un divisor el número NO es primo 
    while d <= n//2 and Primo:
        if n % d == 0: # Se busca algún divisor 
            Primo = False
        d = d + 1 
    return Primo
x = int(input('Entra número natural: ')) 
print('Es',x,'primo?',es_primo(x))