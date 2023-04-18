# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:18:11 2023

@author: Andres Florez
"""

# Juego de adivinar número oculto (generado aleatoriamente) 
from random import randint
oculto = randint(1,100) # Se genera aleatoriamente un número del 1 al 100 
print('Se ha generado un número del 1 al 100')
print('Adivínalo en máximo 7 intentos, ')
intentos = 1
x = int(input('Adivina el número: ')) 
while (x != oculto) and (intentos < 7): 
    if x > oculto: 
        x = int(input('Prueba uno menor(quedan '+str(7-intentos)+' intentos):')) 
    else:
        x = int(input('Prueba uno mayor(quedan '+str(7-intentos)+' intentos):'))
    intentos = intentos + 1
if x == oculto:
    print('Muy bien! lo has conseguido en', intentos, 'intentos')
else:
    print('Lástima, el número oculto era el', oculto)