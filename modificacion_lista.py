# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:07:26 2023

@author: Andres Florez
"""

def FuncSumLstSqr(lst):
     for i in range(len(lst)): 
         lst[i] = lst[i]**2
     return sum(lst)
lista = [1,2,3,4,5]
FuncSumLstSqr(lista)
