# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:15:39 2023

@author: Andres Florez
"""

def cambio_monedas(c):
    e2,c = c // 200, c % 200 
    e, c = c // 100, c % 100 
    c50, c = c // 50, c % 50 
    c20, c = c // 20, c % 20 
    c10, c = c // 10, c % 10 
    c5, c = c // 5, c % 5 
    c2, c = c // 2, c % 2
    return e2, e, c50, c20, c10, c5, c2, c

a = cambio_monedas(367)
print(a)