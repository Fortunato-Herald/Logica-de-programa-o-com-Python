"""
Exercicio 09 - Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
em graus Celsius.
"""

temperatura_fahrenheit= float(input('Temperatura em Fahrenheit: '))

celsius = 5 * ((temperatura_fahrenheit-32) / 9)

print(f'Temperatura em CELSIUS: {celsius:.2f}°')

