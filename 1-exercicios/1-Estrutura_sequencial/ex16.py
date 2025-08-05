"""
Ex 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas 
e o preço total.
"""

# Entrada da área
area = float(input("Informe o tamanho da área a ser pintada (em m²): "))

# Cálculo de litros necessários (1 litro para 3 m²)
litros = area / 3

# Cálculo de latas de 18 litros (arredondar para cima)
latas = litros // 18
if litros % 18 != 0:
    latas = latas + 1

# Conversão para inteiro
latas = int(latas)

# Cálculo do preço
preco_total = latas * 80

# Saída dos resultados
print(f"Quantidade de latas: {latas}")
print(f"Preço total: R$ {preco_total:.2f}")

