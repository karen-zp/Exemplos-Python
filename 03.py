# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:53:01 2024

@author: Karen
"""
import sys

sys.set_int_max_str_digits(30000)

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

print("Recursivo: ", fibonacci_recursivo(10))

def fibonacci_iterativo(n):
    if n <= 1:
        return n

    fib_anterior = 0
    fib_atual = 1

    for _ in range(2, n+1):
        fib_proximo = fib_anterior + fib_atual
        fib_anterior = fib_atual
        fib_atual = fib_proximo

    return fib_atual

print("Iterativo: ", fibonacci_iterativo(10)) 