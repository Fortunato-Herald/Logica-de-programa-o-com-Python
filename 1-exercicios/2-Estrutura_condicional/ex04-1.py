"""
Ex 04.1 - Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""

# letra.lower() → converte para minúsculo, facilitando a comparação.
# 'aeiou' → conjunto de vogais.
# letra.isalpha() → garante que a entrada é uma letra (e não número ou símbolo).
# len(letra) == 1 → garante que só foi digitado um caractere.


letra = input('Digite uma letra: ')

if len(letra) == 1 and letra.isalpha():
    
    if letra.lower() in 'aeiou':
        print('É uma vogal!')
        
    else:
        print('É uma consoante!')
        
else:
    print('Entrada invalida. digite apenas uma letra.')
    
    