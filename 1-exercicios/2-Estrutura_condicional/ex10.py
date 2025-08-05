"""
Ex 10 - Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

# Solicita ao usuário que informe o turno em que estuda
turno = input("Em que turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")

# Converte a letra digitada para maiúscula, para evitar erros com letras minúsculas
turno = turno.upper()

# Verifica qual turno foi digitado e imprime a saudação correspondente
if turno == "M":
    print("Bom Dia!")        # Se for M, imprime "Bom Dia!"
elif turno == "V":
    print("Boa Tarde!")      # Se for V, imprime "Boa Tarde!"
elif turno == "N":
    print("Boa Noite!")      # Se for N, imprime "Boa Noite!"
else:
    print("Valor Inválido!") # Se não for nenhuma das opções válidas, imprime mensagem de erro

