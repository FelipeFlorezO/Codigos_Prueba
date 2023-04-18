# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:16:16 2023

@author: Andres Florez
"""

def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam" 
    spam = "test spam" 
    do_local()
print("After local assignment:", spam) 
print(do_nonlocal())
print("After nonlocal assignment:",spam) 
print(do_global())
print("After global assignment:", spam) 
print(scope_test())
print("In global scope:", spam)