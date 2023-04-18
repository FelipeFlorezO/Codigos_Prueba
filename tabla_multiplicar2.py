# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:32:48 2023

@author: Andres Florez
"""

def TablaMultiplicar(n):
    """Input: entero n 
    Output: void function. Print tabla
    multiplicar de n
    """
    k = 1
    print('Tabla de multiplicar del',n)
    while k <= 10: 
        print(n,'x',k,'=',n*k) 
        k = k + 1
    print()
    
n = int(input('inserte un numero para calcular su tabla de multiplicar: '))
print(TablaMultiplicar(n))