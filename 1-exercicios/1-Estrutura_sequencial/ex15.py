"""
Ex 15 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""

# Entradas
valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

# Cálculos
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

# Saída formatada
print("\n+ Salário Bruto     : R$ {:.2f}".format(salario_bruto))
print("- IR (11%)          : R$ {:.2f}".format(desconto_ir))
print("- INSS (8%)         : R$ {:.2f}".format(desconto_inss))
print("- Sindicato (5%)    : R$ {:.2f}".format(desconto_sindicato))
print("= Salário Líquido   : R$ {:.2f}".format(salario_liquido))
