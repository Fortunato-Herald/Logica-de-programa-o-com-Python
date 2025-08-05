"""
Ex 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes 
situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math  # Importa o módulo math para usar a função sqrt()

# Solicita ao usuário o valor de 'a'
a = float(input("Digite o valor de A: "))

# Verifica se A é zero (não é equação do segundo grau)
if a == 0:
    print("Não é uma equação do segundo grau. Encerrando o programa.")
else:
    # Solicita os valores de b e c
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    # Calcula o delta (discriminante)
    delta = b**2 - 4*a*c

    print(f"\nDelta calculado: {delta:.2f}")

    # Verifica as condições do delta
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: x = {x:.2f}")
    else:
        # Duas raízes reais
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
