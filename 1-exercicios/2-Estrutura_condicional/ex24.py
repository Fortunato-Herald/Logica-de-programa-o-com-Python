"""
Ex 24 - Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

# Lê os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pergunta qual operação deseja realizar
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = input("Digite o número da operação: ")

# Realiza a operação escolhida
if op == '1':
    resultado = num1 + num2
    operacao = "soma"
elif op == '2':
    resultado = num1 - num2
    operacao = "subtração"
elif op == '3':
    resultado = num1 * num2
    operacao = "multiplicação"
elif op == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: divisão por zero!")
        exit()
else:
    print("Operação inválida!")
    exit()

# Verifica se o número é par ou ímpar (considerando somente números inteiros)
if resultado.is_integer():
    if int(resultado) % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
else:
    paridade = "não é inteiro, então não é par nem ímpar"

# Verifica se positivo ou negativo
if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "zero"

# Verifica se é inteiro ou decimal
tipo_num = "inteiro" if resultado.is_integer() else "decimal"

# Exibe o resultado e as características
print(f"\nResultado da {operacao}: {resultado}")
print(f"O número é {paridade}.")
print(f"O número é {sinal}.")
print(f"O número é {tipo_num}.")
