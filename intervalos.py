# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:06:12 2023

@author: Andres Florez
"""

x = float(input('Inserte un valor para x: '))
y = float(input('Inserte un valor para y: '))

if not(x >= 100 and x <= 200):
    print('x está por fuera del intervalo')
else:
    print('x está en el intervalo')
if not(y >= 20 and y <= 40):
    print('y está por fuera del intervalo')
else:
    print('y está en el intervalo')