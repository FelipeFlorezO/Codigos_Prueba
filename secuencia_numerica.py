# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:37:39 2023

@author: Andres Florez
"""

# Mostrar los N primeros números naturales en forma descendiente
N = int(input('Entra un número natural: '))
i = N
while i >= 1:
    print(i, end =' ')
    i = i - 1
print('\nHemos mostrado',N,'números naturales decreciendo')