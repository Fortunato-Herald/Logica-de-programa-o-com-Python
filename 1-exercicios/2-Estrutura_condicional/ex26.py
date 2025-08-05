"""
Ex 26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:

até 20 litros: desconto de 3% por litro
acima de 20 litros: desconto de 5% por litro
Gasolina: - até 20 litros: desconto de 4% por litro - acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte 
forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

# Lê o tipo de combustível e a quantidade em litros
combustivel = input("Tipo de combustível (A - Álcool, G - Gasolina): ").upper()
litros = float(input("Quantidade de litros vendidos: "))

# Define preço por litro conforme o combustível
if combustivel == 'A':
    preco_litro = 1.90
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
elif combustivel == 'G':
    preco_litro = 2.50
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
else:
    print("Tipo de combustível inválido!")
    exit()

# Calcula valor total e valor com desconto
valor_total = litros * preco_litro
valor_desconto = valor_total * desconto
valor_final = valor_total - valor_desconto

# Exibe o resultado
print(f"Valor a pagar: R$ {valor_final:.2f}")
