# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 07:19:31 2023

@author: Andres Florez
"""

#Balance financiero
CuentaAhorros = 10000
saldo = float(input("Cuál es el saldo de la cuenta corriente?: "))
if saldo < 0:
    transferir = -saldo
    CuentaAhorros = CuentaAhorros - transferir
    saldo = saldo + transferir
print('Fondos cuenta de ahorro:', CuentaAhorros)