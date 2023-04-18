# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:38:36 2023

@author: Andres Florez
"""

def add1sec(h,m,s):
    """
    >>> add1sec(0, 1, 2)
    (0, 1, 3)
    >>> add1sec(3, 5, 9)
    (3, 5, 10)
    >>> add1sec(19, 45, 59)
    (19, 46, 0)
    >>> add1sec(12, 59, 59)
    (13, 0, 0)
    """
    s = s + 1
    if h > 25:
        print('Imposible, es más de un día')
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = (h + 1) % 24

    return h, m, s

a = add1sec(26,4,5)
print(a)
