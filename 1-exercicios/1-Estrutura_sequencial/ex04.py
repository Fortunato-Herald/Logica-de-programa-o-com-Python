"""
Exercício 04 - Faça um programa que peça as 4 notas bimestrais e mostre a média.
"""

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Nota 1: {nota1}, Nota 2: {nota2}, Nota 3: {nota3},  Nota 4: {nota4}')
print(f'MEDIA: {media}')