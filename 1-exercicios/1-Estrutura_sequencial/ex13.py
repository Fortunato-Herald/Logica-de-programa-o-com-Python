"""
Ex 13 - Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para 
Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
"""

# Entrada do usuário
gb = float(input("Digite o tamanho do arquivo em Gigabytes (GB): "))

# Conversões
mb = gb * 1024
kb = gb * 1024 * 1024

# Saída dos resultados
print(f"\nTamanho em Megabytes: {mb:.2f} MB")
print(f"Tamanho em Kilobytes: {kb:.2f} KB")
