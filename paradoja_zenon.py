# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:29:34 2023

@author: Andres Florez
"""

# Paradoja de la dicotimía de Zenon (términos definidos)
n = int(input('Entra el número de términos a calcular:')) 
suma = 0
for i in range(1, n+1):
    suma = suma + 1/2**i
print('El valor de la sumatoria es', suma)