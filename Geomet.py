# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:20:35 2023

@author: Andres Florez
"""

from math import pi 
def AreaCirc(radio):
    return pi*radio**2 
def PerimCirc(radio):
    return 2*pi*radio
def VolCilindro(radio, h):
    return h*pi*radio**2
def AreaRect(b, h): 
    return b*h
def PerimRect(b, h):
    return 2*(b+h)
def VolOrtoed(b, h, a): 
    return b*h*a