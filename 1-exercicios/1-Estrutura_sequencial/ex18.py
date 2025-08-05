"""
Ex 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

# Entrada dos dados
tamanho_arquivo_mb = float(input("Informe o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Informe a velocidade da internet (em Mbps): "))

# Conversão de Mbps para MBps (1 Byte = 8 bits)
velocidade_MBps = velocidade_mbps / 8

# Cálculo do tempo em segundos
tempo_segundos = tamanho_arquivo_mb / velocidade_MBps

# Conversão para minutos
tempo_minutos = tempo_segundos / 60

# Saída com 2 casas decimais
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")
