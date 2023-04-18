# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 11:02:14 2023

@author: Andres Florez
"""

# Mostrar los N primeros números naturales en forma descendiente (for)
N = int(input('Entra un número natural: ')) 
for i in range(N, 0, -1):
    print(i, end =' ')
print('\nHemos mostrado',N,'números naturales decreciendo')