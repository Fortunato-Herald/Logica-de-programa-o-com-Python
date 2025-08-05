"""
Exercício 08 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

gh = float(input('Ganho por hora: '))
ht = int(input('Horas trabalhadas: '))

sal = gh * ht

print('Seu salario: {} R$'.format(sal))