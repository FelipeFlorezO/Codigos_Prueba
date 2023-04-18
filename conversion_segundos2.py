# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:04:00 2023

@author: Andres Florez
"""

# Programa para convertir segundos a días, horas, minutos, y segundos
s = int(input("Entra segundos: "))
print(s, 'segundos son:') 
m = s//60
s = s%60 
h = m//60 
m = m%60
d = h // 24 
h = h % 24
print(d, "días,",h,"horas,",m, "minutos y", s, "segundos")