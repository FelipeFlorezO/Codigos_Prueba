# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:45:46 2023

@author: Andres Florez
"""

#Algoritmo de Herón. Cálculo de la raíz cuadrada

def raiz(x, epsilon=1e-10):
    """Raiz cuadrada, método de Herón
    print(raiz(9))
    3.0
    """
    g = x/2 #El valor inicial g (guess), g0, puede ser x/2
    dif = g*g - x #Diferencia entre el valor de raíz g0 propuesto y el real
    while abs(dif) > epsilon:
        g = (g + x/g)/2
        dif = g*g - x
    return g
a = float(input('Entra un numero para hallar su raíz cuadrada: '))
while a < 0:
    a = float(input('El numero debe ser positivo!!! '))
r = raiz(a)
print('La raíz cuadrada de ',a, 'es',r )
from math import sqrt
print('La raiz cuadrada con fun sqrt de ',a, 'es', sqrt(a))