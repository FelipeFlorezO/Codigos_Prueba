# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:03:23 2023

@author: Andres Florez
"""

def calificacion(nota): 
    '''Muestra la calificación
    a partir de la nota numérica 
    Ejemplos:
    >>> calificacion(3) 
    'Suspenso'
    >>> calificacion(5) 
    'Aprobado'
    >>> calificacion(7.5) 
    'Notable'
    >>> calificacion(9.5) 
    'Sobresaliente'
    '''
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

nota = float(input('Inserte su calificación'))
print(calificacion(nota))