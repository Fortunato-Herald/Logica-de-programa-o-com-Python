"""
Ex 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                Até 5 Kg                Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um 
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

# Lê as quantidades de morango e maçã em kg
kg_morango = float(input("Quantidade de morangos (Kg): "))
kg_maca = float(input("Quantidade de maçãs (Kg): "))

# Define preço por kg para morango
if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

# Define preço por kg para maçã
if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Calcula total por fruta
total_morango = preco_morango * kg_morango
total_maca = preco_maca * kg_maca

# Soma total de kg e valor total
total_kg = kg_morango + kg_maca
total_compra = total_morango + total_maca

# Verifica se tem direito a desconto
if total_kg > 8 or total_compra > 25:
    desconto = total_compra * 0.10
else:
    desconto = 0

# Calcula valor final a pagar
valor_final = total_compra - desconto

# Exibe o resultado
print(f"Total a pagar: R$ {valor_final:.2f}")

