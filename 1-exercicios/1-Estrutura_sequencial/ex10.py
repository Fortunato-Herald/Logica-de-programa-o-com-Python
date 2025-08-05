"""
Exercício 10 - Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus 
Fahrenheit.
"""

temperatura_celsius = float(input('Temperatura em Celsius: '))

fahrenheit = (temperatura_celsius * 9/5) + 32

print('Temperatura em Fahrentheit: {:.2f}°'.format(fahrenheit))

