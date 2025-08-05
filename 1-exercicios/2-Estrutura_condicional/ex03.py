"""
Ex 03 - Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input('Digite [F] - Feminino ou [M] - Masculino: ')

if (letra == 'M' or letra == 'm'):
    print('Masculino')


elif (letra == 'F' or letra == 'f'):
    print('Feminino')
    
else:
    print('Sexo invalido!')