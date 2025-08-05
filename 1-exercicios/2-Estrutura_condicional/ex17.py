"""
Ex 17 - Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este 
ano é ou não bissexto.
"""

# Regras para ano bissexto:
# Um ano é bissexto se:
# É divisível por 4 e
# não é divisível por 100, ou
# é divisível por 400 

# Solicita ao usuário que digite o ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto com base nas regras
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")