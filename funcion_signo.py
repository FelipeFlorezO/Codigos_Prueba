# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:47:40 2023

@author: Andres Florez
"""

# Función signo(x), version elif 
x = float(input("Entra x: ")) 
if x < 0:
    signo = -1 
elif x == 0:
    signo = 0 
else:
    signo = 1
print('El signo de', x, '=', signo)