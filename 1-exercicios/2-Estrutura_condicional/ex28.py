"""
Ex 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não 
há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá 
ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, 
preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

# Exibe o menu de carnes
print("===== Hipermercado Tabajara =====")
print("Promoção de Carnes:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

# Solicita o tipo de carne
tipo_carne = input("Escolha o tipo de carne (1, 2 ou 3): ")
quantidade = float(input("Informe a quantidade (Kg): "))

# Solicita o tipo de pagamento
pagamento = input("Pagamento com Cartão Tabajara? (S/N): ").upper()

# Determina o nome da carne e preço por Kg
if tipo_carne == '1':
    nome_carne = "Filé Duplo"
    preco_kg = 4.90 if quantidade <= 5 else 5.80
elif tipo_carne == '2':
    nome_carne = "Alcatra"
    preco_kg = 5.90 if quantidade <= 5 else 6.80
elif tipo_carne == '3':
    nome_carne = "Picanha"
    preco_kg = 6.90 if quantidade <= 5 else 7.80
else:
    print("Tipo de carne inválido!")
    exit()

# Calcula total e possível desconto
preco_total = quantidade * preco_kg
desconto = preco_total * 0.05 if pagamento == 'S' else 0
total_a_pagar = preco_total - desconto

# Define forma de pagamento
forma_pagamento = "Cartão Tabajara" if pagamento == 'S' else "Outro"

# Exibe o cupom fiscal
print("\n===== CUPOM FISCAL =====")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {total_a_pagar:.2f}")
