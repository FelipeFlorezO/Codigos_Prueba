# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:03:05 2023

@author: Andres Florez
"""

# Calculo de la suma de los primeros n números (versión for) 
n = int(input('Entra un número natural: '))
suma = 0
for i in range(1, n+1): 
    suma = suma + i
print('La suma de los números naturales hasta',n,'es', suma)