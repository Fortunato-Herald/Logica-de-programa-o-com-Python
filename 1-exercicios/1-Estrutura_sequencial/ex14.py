"""
Ex 14 - João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia 
a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens 
adequadas.
"""

# Entrada do peso dos peixes
peso = float(input("Digite o peso de peixes trazido (em kg): "))

# Limite permitido
limite = 50.0

# Cálculo do excesso (sem if/else, usando max para garantir que nunca seja negativo)
excesso = max(0, peso - limite)

# Cálculo da multa
multa = excesso * 4.00

# Exibição dos resultados
print(f"\nPeso informado: {peso:.2f} kg")
print(f"Excesso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
