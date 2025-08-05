"""
Ex 09 - Faça um programa que leia três números e mostre-os em ordem decrescente:
"""

#  Utilizando lista.

# Leitura dos numeros.
num1 = float(input('Numero 1: '))
num2 = float(input('Numero 2: '))
num3 = float(input('Numero 3: '))

# Coloca os números em ima lista.
numeros = [num1, num2, num3]

# Coloca em ordem decrescente.
numeros.sort(reverse=True)

# Saída
print('Numeros em ordem decrescente: ', numeros)
