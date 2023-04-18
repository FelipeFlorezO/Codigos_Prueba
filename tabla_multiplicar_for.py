# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:51:08 2023

@author: Andres Florez
"""

# Tabla de multiplicar (del 1 al 10) del número introducido (versión for)
n = int(input('Entra un número entero: ')) 
for k in range(1, 11):
    print(n,'x',k,'=',n*k)
print('Hemos mostrado la tabla de multiplicar del',n)