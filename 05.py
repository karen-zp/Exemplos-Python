# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:15:05 2024

@author: Karen
"""

#lista
numeros = list(range(1, 11))

#verifica se está vazia
if not numeros:
    print("Lista está vazia")
else:
    print("Lista não vazia")
    
print("Elementos: ", numeros)


primeiros = numeros[:3]
print("3 Primeiros: ", primeiros)

ultimos = numeros[-3:]
print("3 ultimos: ", ultimos)

#removendo elementos da lista
while numeros:
    elemento = numeros.pop(0)
    print(f"Removido: {elemento}")
    print(f"Lista atual: {numeros}")
    
if not numeros:
    print("Lista está vazia")
else:
    print("Lista não vazia")
     
print("Elementos: ", numeros) 
