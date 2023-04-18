# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:53:27 2023

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
        calif = "Suspenso"
    else:
        if nota < 7:
            calif = "Aprobado"
        else:
            if nota < 9:
                calif = "Notable"
            else:
                calif = "Sobresaliente"
    return calif


nota = float(input('Inserte su calificacion: '))
print(calificacion(nota))