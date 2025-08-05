"""
Ex 08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato:
"""

# Leitura dos produtos.
prod1 = float(input('Preço 1: '))
prod2 = float(input('Preço 2: '))
prod3 = float(input('Preço 3: '))

# Verifica preço.
if prod1 < prod2 and prod1 < prod3:
    menor = prod1

elif prod2 < prod1 and prod2 < prod3:
    menor = prod2

else:
    menor = prod3

print('O produto mais barato é o que custa {} R$'.format(menor))