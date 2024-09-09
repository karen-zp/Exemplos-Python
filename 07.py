# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:33:58 2024

@author: Karen
"""
def mostrar_primeiros_e_ultimos_itens(dicionario, N):
    chaves = list(dicionario.keys())
    valores = list(dicionario.values())
    
    primeiros_n = {chaves[i]: valores[i] for i in range(min(N, len(chaves)))}
    ultimos_n = {chaves[i]: valores[i] for i in range(max(len(chaves) - N, 0), len(chaves))}
    
    return primeiros_n, ultimos_n

dicionario = {'a': 1, 'b': 2, 'c': 3}
primeiros, ultimos = mostrar_primeiros_e_ultimos_itens(dicionario, 2)
print("Primeiros N itens:", primeiros)
print("Ultimos N itens:", ultimos)

def inverter_chaves_e_valores(dicionario):
    return {valor: chave for chave, valor in dicionario.items()}

dicionario = {'a': 1, 'b': 2, 'c': 3}
invertido = inverter_chaves_e_valores(dicionario)
print("Dicionario invertido:", invertido)
