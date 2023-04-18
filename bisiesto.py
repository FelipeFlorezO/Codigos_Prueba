# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:32:44 2023

@author: Andres Florez
"""

def bisiesto(A):
    """Función que devuelve si un año es bisiesto o no 
    """
    return A % 400 == 0 or (A % 4 == 0 and A % 100 != 0)
year = int(input("Entra un año: "))
if bisiesto(year): 
    print(year,'es bisiesto')
else:
    print(year,'NO es bisiesto')