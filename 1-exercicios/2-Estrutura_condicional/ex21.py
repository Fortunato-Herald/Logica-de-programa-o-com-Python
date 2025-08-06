"""
Ex 21 - Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 
100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade
de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 
5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas 
de 10, uma nota de 5 e quatro notas de 1.
"""

# Ex 21 - Caixa eletrônico:
# O programa solicita ao usuário um valor de saque entre 10 e 600 reais
# e calcula a quantidade de notas de 100, 50, 10, 5 e 1 real necessárias.

# Solicita o valor do saque ao usuário
valor = int(input("Digite o valor do saque (10 a 600): "))

# Verifica se o valor está dentro do intervalo permitido
if valor < 10 or valor > 600:
    print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
else:
    # Calcula a quantidade de notas de 100
    notas_100 = valor // 100
    resto = valor % 100  # Armazena o valor restante após as notas de 100

    # Calcula a quantidade de notas de 50
    notas_50 = resto // 50
    resto = resto % 50  # Atualiza o valor restante

    # Calcula a quantidade de notas de 10
    notas_10 = resto // 10
    resto = resto % 10  # Atualiza o valor restante

    # Calcula a quantidade de notas de 5
    notas_5 = resto // 5
    notas_1 = resto % 5  # O restante agora são notas de 1 real

    # Exibe a quantidade de cada nota fornecida
    print(f"Notas de 100: {notas_100}")
    print(f"Notas de 50: {notas_50}")
    print(f"Notas de 10: {notas_10}")
    print(f"Notas de 5: {notas_5}")
    print(f"Notas de 1: {notas_1}")

