# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:30:54 2023

@author: Andres Florez
"""

# Tabla de multiplicar (del 1 al 10) del número introducido
n = int(input('Entra un número entero:')) 
k = 1
while k <= 10: 
    print(n,'x',k,'=',n*k) 
    k = k + 1
print('Tabla de multiplicar del',n)