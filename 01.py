# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:33:14 2024

@author: Karen
"""

#hello world
print("Hello World!")

#print variavel
nome = "Karen"
print("Hello", nome)

#função de hello world
def hello_world():
    print("Hello World!")

hello_world()

#retorna 1 variavel
def retorna_nome(nome):
    return nome

nome_retornado = retorna_nome("neraK")
print("Nome retornado:", nome_retornado)

#retorna 2 variaveis
def retorna_nome_e_idade(nome, idade):
    return nome, idade

nome_retornado, idade_retornada = retorna_nome_e_idade("Blabla", 30)
print("Nome retornado:", nome_retornado)
print("Idade retornada:", idade_retornada) 



