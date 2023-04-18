# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:08:33 2023

@author: Andres Florez
"""

# Año bisiesto (leap year): año que es divisble por 400, o que sea divisible # por 4 exceptuando los divisibles por 100.
year = int(input("Entra un año "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    BIS = True 
else:
    BIS = False
print('¿Es ',year,'bisiesto?',BIS)