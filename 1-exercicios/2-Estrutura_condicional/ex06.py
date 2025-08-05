"""
Ex 06 - Faça um programa que leia três números e mostre o maior deles:
"""

# Leitura dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificações de igualdade
if num1 == num2 == num3:
    print("Todos os três números são iguais:", num1)

elif num1 == num2 and num1 > num3:
    print("O maior número é:", num1, "e aparece duas vezes (num1 e num2).")

elif num1 == num3 and num1 > num2:
    print("O maior número é:", num1, "e aparece duas vezes (num1 e num3).")

elif num2 == num3 and num2 > num1:
    print("O maior número é:", num2, "e aparece duas vezes (num2 e num3).")

# Verificação do maior número único
elif num1 > num2 and num1 > num3:
    print("O maior número é:", num1)

elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)

else:
    print("O maior número é:", num3)