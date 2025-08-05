"""
Ex 07 - Faça um programa que leia três números e mostre o maior e o menor deles:
"""

# Leitura dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificação de igualdade entre todos
if num1 == num2 == num3:
    print("Todos os três números são iguais:", num1)

# Verificação se dois são iguais e maiores ou menores
elif num1 == num2 and num1 > num3:
    print("O maior número é:", num1, "(repetido duas vezes)")
    print("O menor número é:", num3)

elif num1 == num3 and num1 > num2:
    print("O maior número é:", num1, "(repetido duas vezes)")
    print("O menor número é:", num2)

elif num2 == num3 and num2 > num1:
    print("O maior número é:", num2, "(repetido duas vezes)")
    print("O menor número é:", num1)

elif num1 == num2 and num1 < num3:
    print("O menor número é:", num1, "(repetido duas vezes)")
    print("O maior número é:", num3)

elif num1 == num3 and num1 < num2:
    print("O menor número é:", num1, "(repetido duas vezes)")
    print("O maior número é:", num2)

elif num2 == num3 and num2 < num1:
    print("O menor número é:", num2, "(repetido duas vezes)")
    print("O maior número é:", num1)

# Caso todos os números sejam diferentes
else:
    maior = num1
    menor = num1

    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3

    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print("O maior número é:", maior)
    print("O menor número é:", menor)
