# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:09:31 2024

@author: Karen
"""

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def sequencia_fatorial(n):
    return [fatorial(i) for i in range(n+1)]

print("Fatorial: ", sequencia_fatorial(10))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sequencia_fibonacci(n):
    return [fibonacci(i) for i in range(n+1)]

print("Fibonacci: ", sequencia_fibonacci(10)) 