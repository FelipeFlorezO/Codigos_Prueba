# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:53:34 2023

@author: Andres Florez
"""

def ejecutar_test():
    def do_local():
        test = 'local test'
    def do_nonlocal():
        nonlocal test
        test = 'nonlocal test'
    def do_global():
        global test
test = 'global test'
test = 'prueba test'

print('Declaración Local:', test)

print('Declaración No Local:', test)

print('Declaración Global:', test)

print('Global:', test)