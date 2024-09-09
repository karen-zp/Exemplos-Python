# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:44:14 2024

@author: Karen
"""

def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)
    
print("Recursivo: ", fatorial_recursivo(5))

def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print("Iterativo: ", fatorial_iterativo(5))