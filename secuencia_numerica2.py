# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:39:11 2023

@author: Andres Florez
"""

def MostrarNdesc(n):
    """Muestra n naturales descendiendo. Función No productiva """
    i = n
    while i >= 1:
        print(i, end =' ') 
        i = i - 1
        print()

n = int(input('Inserte un número'))
print(MostrarNdesc(n))