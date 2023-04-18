# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:28:45 2023

@author: Andres Florez
"""

def juego_acertar_número():
    """
    Sin doctest pues se generan números aleatorios
    >>>juego_acertar_número() 
    """
    from random import randint
    oculto = randint(1, 100)
    print('He pensado un número entre 1 y 100, aciértalo') 
    acertar = int(input("Di un número entre 1 y 100: ")) 
    intentos = 1
    while acertar != oculto and intentos < 7:
        if acertar > oculto:
            acertar = int(input('Es menor (quedan '+str(7-intentos)+' intentos):'))
        else:
            acertar = int(input('Es mayor (quedan '+str(7-intentos)+' intentos):'))
        intentos += 1
    if acertar == oculto:
        print('Muy bien! lo has conseguido en', intentos, 'intentos')
    else:
        print('Lástima, el número oculto era el', oculto)
        
print(juego_acertar_número())