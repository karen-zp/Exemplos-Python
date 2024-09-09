# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:22:05 2024

@author: Karen
"""
#dicionario de 10 numeros
dicionario_numeros = {}
for i in range(1, 11):
    dicionario_numeros[i] = i

#listar numeros
print("Numeros do dicionário: ")
for chave, valor in dicionario_numeros.items():
    print(valor)

#listar 3 primeiros e 3 ultimos
print("\n3 primeiros: ")
for chave, valor in list(dicionario_numeros.items())[:3]:
    print(valor)

print("\n3 ultimos: ")
for chave, valor in list(dicionario_numeros.items())[-3:]:
    print(valor)

#dicio com 5 nomes
dicionario_nomes = {}
nomes = ["Karen", "Heygdio", "Ana", "Carol", "Pedro"]
for i, nome in enumerate(nomes):
    dicionario_nomes[i+1] = nome

#listar os nomes
print("\nNomes do dicionário:")
for chave, valor in dicionario_nomes.items():
    print(valor)

#dicio com nomes e numeros aleatorios
import random
dicionario_nomes_numeros = {}
for nome in nomes:
    dicionario_nomes_numeros[nome] = random.randint(1, 100)

#imprime ultimo dicio
print("\nDicionario de nomes e numeros aleatorios: ")
for chave, valor in dicionario_nomes_numeros.items():
    print(f"{chave}: {valor}") 