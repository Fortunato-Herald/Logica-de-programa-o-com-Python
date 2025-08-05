"""
Ex 25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder 
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
"Assassino". Caso contrário, ele será classificado como "Inocente".
"""

respostas_positivas = 0

resposta = input("Telefonou para a vítima? (S/N): ").strip().upper()
if resposta == 'S':
    respostas_positivas += 1

resposta = input("Esteve no local do crime? (S/N): ").strip().upper()
if resposta == 'S':
    respostas_positivas += 1

resposta = input("Mora perto da vítima? (S/N): ").strip().upper()
if resposta == 'S':
    respostas_positivas += 1

resposta = input("Devia para a vítima? (S/N): ").strip().upper()
if resposta == 'S':
    respostas_positivas += 1

resposta = input("Já trabalhou com a vítima? (S/N): ").strip().upper()
if resposta == 'S':
    respostas_positivas += 1

if respostas_positivas == 5:
    print("Classificação: Assassino")
elif respostas_positivas >= 3:
    print("Classificação: Cúmplice")
elif respostas_positivas == 2:
    print("Classificação: Suspeita")
else:
    print("Classificação: Inocente")
