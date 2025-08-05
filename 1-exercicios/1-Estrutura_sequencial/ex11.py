"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
"""

# Entradas
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

# Cálculos
resultado1 = (2 * num1) * (num2 / 2)
resultado2 = (3 * num1) + num3
resultado3 = num3 ** 3

# Saídas
print(f"\n1. O produto do dobro do primeiro com metade do segundo: {resultado1}")
print(f"2. A soma do triplo do primeiro com o terceiro: {resultado2}")
print(f"3. O terceiro número elevado ao cubo: {resultado3}")
