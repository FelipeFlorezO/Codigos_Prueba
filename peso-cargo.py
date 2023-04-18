# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 08:07:43 2023

@author: Andres Florez
"""

# Exceso de peso
peso = float(input("Cuántos quilos pesa su maleta?:")) 
if peso > 23:
    text = 'Su maleta excede el peso permitido, tendrá un cargo de 30 euros'
else:
    text = 'Su maleta tiene un peso correcto' 
print(text)