"""
Ex 23 - Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função 
de arredondamento.
"""

num = float(input("Digite um número: "))

# Arredonda o número para inteiro
num_arredondado = round(num)

# Compara o número com o arredondado para decidir
if num == num_arredondado:
    print("O número é inteiro.")
else:
    print("O número é decimal.")

