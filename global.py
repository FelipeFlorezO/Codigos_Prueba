# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:15:31 2023

@author: Andres Florez
"""

def f(x):
    global a
    y = a*x 
    a = 3 
    return y
a = 7
print('Función:',f(4))
print('Valor de la variable global a:',a)