"""
13 - Faça um programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

# Solicita ao usuário que informe um número de 1 a 7
print('Digite um numero')
print('Escolha uma opção')

numero = int(input('1-Domingo, \n2-Segunda-Feira, \n3-Terça-Feira, \n4-Quarta-Feira, \n5-Quinta-Feira, \n6-Sexta-feira, \n7-Sabado \n'))

# Verifica qual é o dia correspondente
if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-Feira')
elif numero == 3:
    print('Terça-Feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-Feira')
elif numero == 6:
    print('Sexta-Feira')
elif numero == 7:
    print('Sabado')
else:
    print('Opção Invalida!!!')
    print('Digite um numero de 1 a 7')
