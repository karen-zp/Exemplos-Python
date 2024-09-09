# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:55:16 2024

@author: Karen
"""

def analisar_notas(dicionario_notas):
    medias = {}
    notas_altas = {}
    notas_baixas = {}
    
    for aluno, notas in dicionario_notas.items():
        media = sum(notas) / len(notas)
        medias[aluno] = media
        notas_altas[aluno] = max(notas)
        notas_baixas[aluno] = min(notas)
    
    aluno_maior_media = max(medias, key=medias.get)
    aluno_menor_media = min(medias, key=medias.get)
    
    print("Média de cada aluno:")
    for aluno, media in medias.items():
        print(f"{aluno}: {media:.2f}")
    
    print("\nNota mais alta e mais baixa de cada aluno:")
    for aluno in dicionario_notas:
        print(f"{aluno} - Nota mais alta: {notas_altas[aluno]}, Nota mais baixa: {notas_baixas[aluno]}")
    
    print(f"\nAluno com a maior média: {aluno_maior_media} ({medias[aluno_maior_media]:.2f})")
    print(f"Aluno com a menor média: {aluno_menor_media} ({medias[aluno_menor_media]:.2f})")

dicionario_notas = {
    'João': [10, 5, 8],
    'Maria': [9, 9, 9],
    'José': [8, 7, 6]
}

analisar_notas(dicionario_notas)
