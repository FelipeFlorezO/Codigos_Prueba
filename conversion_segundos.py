# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 18:59:01 2023

@author: Andres Florez
"""

# Permite convertir los segundos a días, horas, minutos, y segundos
s = int(input("Segundos ejecutados: "))
print(s, "segundos: ")
m = s//60
s = s%60
h = m//60
m = m%60
d = h // 24
h = h % 24
print(d, "días, ", h, "horas, ", m, "minutos y", s, "segundos")