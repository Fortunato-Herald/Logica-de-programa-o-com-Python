"""
Ex 12 - Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para 
Megabytes, usando a seguinte fórmula:
"""

# Entrada do usuário
gb = float(input("Digite o tamanho do arquivo em Gigabytes (GB): "))

# Conversão para Megabytes
mb = gb * 1024

# Saída do resultado
print(f"\nTamanho em Megabytes: {mb:.2f} MB")
