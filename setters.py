# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:02:08 2023

@author: Andres Florez
"""

class cuadrado():
  def __init__(self, diagonal):
    #self.__diagonal = diagonal
    self.cuadrado = diagonal
    
  @property
  def cuadrado(self):
    print("Estoy dando la diagonal")
    return self.diagonal

  @cuadrado.setter
  def cuadrado(self, diagonal):
    if diagonal >= 0:
      self.diagonal = diagonal
    else:
      print("La diagonal debe ser positiva")
      self.diagonal = 0
        
x = cuadrado(2)
print(x.cuadrado)
y = cuadrado(-2)
print(y.cuadrado)