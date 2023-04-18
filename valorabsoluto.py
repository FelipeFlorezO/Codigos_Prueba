# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:17:38 2023

@author: Andres Florez
"""

x = float(input("Entra un número: "))
if x < 0:
    x = -x
print(f'El valor absoluto es:':.2f{x})