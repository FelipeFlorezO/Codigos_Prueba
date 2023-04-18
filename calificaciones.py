# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:49:40 2023

@author: Andres Florez
"""

print('Programa que convierte una nota numérica a cualitativa')
nota = float(input('Nota numérica: '))
if (nota <0) or (nota > 10): 
    calif = 'Nota no válida'
elif nota < 5:
    calif = 'Suspenso (SS)' 
elif nota < 7:
    calif = 'Aprobado (AP)' 
elif nota < 9:
    calif = 'Notable (NT)'
else:
    calif = 'Sobresaliente (SB)'
    
print('La nota', nota, 'equivale a', calif)