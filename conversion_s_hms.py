# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:07:59 2023

@author: Andres Florez
"""

# Programa para convertir segundos a horas, minutos, y segundos
def pasar_s_a_hms(s):
    '''convertir segundos a horas, minutos, y segundos. Ejemplos:
    >>> pasar_s_a_hms(61) 
    (0, 1, 1)
    >>> pasar_s_a_hms(60)
    (0, 1, 0)
    >>> pasar_s_a_hms(3600) 
    (1, 0, 0)
    >>> pasar_s_a_hms(123456) 
    (34, 17, 36)
    '''
    m = s//60
    s = s%60
    h = m//60 
    m = m%60
    return h, m, s

if __name__ == "__main__":
    print(pasar_s_a_hms(10)) 
    print(pasar_s_a_hms(75)) 
    print(pasar_s_a_hms(3699)) 
    
import doctest 
doctest.testmod()
print(doctest.testmod())