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

#Ejercicio 2
def algoritmo_2(num, total_compra):
    if num >= 74:
        desc = total_compra * 0.2
    else:
        desc = total_compra * 0.15

    return desc

#Ejercicio 3
def algoritmo_3(mon_fianza):
    if mon_fianza <= 50000:
        cuota = mon_fianza * 0.03
    else:
        cuota = mon_fianza * 0.02

    return cuota

#Ejercicio 4
def algoritmo_4(prom, gan_diaria):
    if prom > 170:
        multa = gan_diaria / 2
        perd = (gan_diaria * 5) + multa

        return f'Multa: {multa}... Perdida: {perd}'

    return 'Sin sancion'

#Ejercicio 5
def algoritmo_5(prec, deval, increm):
    can_deval = -1 * (((prec * deval) * deval) * deval)
    can_increm = (((prec * increm) * increm) * increm)

    if can_deval < (can_increm / 2):
        return True

    return False

#Ejercicio 6
def algoritmo_6(cant):
    total = cant * 11000

    if cant < 5:
        desc = total * 0.1
    elif cant >= 5 and cant < 10:
        desc = total * 0.2
    elif cant > 10:
        desc = total * 0.4

    return desc

#Ejercicio 7
def algoritmo_7(prec, marc):
    desc = 0

    if marc == 'NOSY':
        desc += prec * 0.05

    if prec >= 2000:
        desc += prec * 0.1

    total = (prec - desc) * 1.16
    return total

#Ejercicio 8
def algoritmo_8(total):
    if total > 500000:
        inv = total * 0.55
        prest = total * 0.3
        cred = total * 0.15
    else:
        inv = total * 0.7
        cred = total * 0.3
        prest = 0

    intereses = cred * 0.2

    return inv, prest, cred, intereses