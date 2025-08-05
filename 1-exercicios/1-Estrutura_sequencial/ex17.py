"""
Ex 17 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias.
"""

import math

# Entrada do usuário
area = float(input("Informe o tamanho da área a ser pintada (em m²): "))

# Adiciona 10% de folga
area_com_folga = area * 1.1

# Calcula a quantidade de litros necessários
litros_necessarios = area_com_folga / 6

# 1. Apenas latas de 18 litros
latas = math.ceil(litros_necessarios / 18)
preco_latas = latas * 80

# 2. Apenas galões de 3,6 litros
galoes = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes * 25

# 3. Mistura de latas e galões (para menor desperdício)
latas_mistas = int(litros_necessarios // 18)
restante = litros_necessarios % 18
galoes_mistos = math.ceil(restante / 3.6)
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

# Resultados
print("\nSituação 1: Apenas latas de 18 litros")
print(f"Quantidade: {latas} lata(s)")
print(f"Preço total: R$ {preco_latas:.2f}")

print("\nSituação 2: Apenas galões de 3,6 litros")
print(f"Quantidade: {galoes} galão(ões)")
print(f"Preço total: R$ {preco_galoes:.2f}")

print("\nSituação 3: Mistura (mínimo desperdício)")
print(f"Quantidade: {latas_mistas} lata(s) e {galoes_mistos} galão(ões)")
print(f"Preço total: R$ {preco_misto:.2f}")
