# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:00:17 2021

@author: Lenovo
"""
#Ejercicio 1
def algoritmo_1(num_camisa, total_compra):
    if num_camisa >= 3:
        desc = total_compra * 0.3
    else:
        desc = total_compra * 0.1

    total_pagar = total_compra - desc

    return desc, total_pagar