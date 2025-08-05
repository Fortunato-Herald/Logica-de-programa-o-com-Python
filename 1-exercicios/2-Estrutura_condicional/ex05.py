"""
Ex 05 - Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
"""

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media == 10:
    print(f'MEDIA: {media}, Aluno aprovado com distinção!!!')

elif media >= 7 and media < 10:
    print(f'MEDIA: {media},  Aluno aprovado!!')

else:
    print(f'MEDIA: {media}, Aluno reprovado!')
    