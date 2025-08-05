"""
Ex 12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de 
Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário 
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
trabalhadas no mês.
Desconto do IR: - Salário Bruto até 900 (inclusive) - isento - Salário Bruto até 1500 (inclusive) - 
desconto de 5% - Salário Bruto até 2500 (inclusive) - desconto de 10% - Salário Bruto acima de 2500 - 
desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
quantidade de hora é 220.
"""

# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

# Solicita ao usuário o valor da hora e a quantidade de horas trabalhadas
valor_hora = float(input("Informe o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Define o percentual do Imposto de Renda (IR) de acordo com o salário bruto
if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

# Percentuais fixos
inss_percentual = 10   # INSS (previdência)
fgts_percentual = 11   # FGTS (empresa deposita, não desconta)

# Calcula os valores de cada item
ir = salario_bruto * (ir_percentual / 100)
inss = salario_bruto * (inss_percentual / 100)
fgts = salario_bruto * (fgts_percentual / 100)

# Calcula total de descontos e salário líquido
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

# Exibe os resultados formatados
print("\n===== Folha de Pagamento =====")
print(f"Salário Bruto: ({valor_hora:.2f} * {horas_trabalhadas})          : R$ {salario_bruto:.2f} R$")
print(f"(-) IR ({ir_percentual}%)                            : R$ {ir:.2f} R$")
print(f"(-) INSS ({inss_percentual}%)                          : R$ {inss:.2f} R$")
print(f"FGTS ({fgts_percentual}%)                              : R$ {fgts:.2f} R$")
print(f"Total de descontos                      : R$ {total_descontos:.2f} R$")
print(f"Salário Líquido                         : R$ {salario_liquido:.2f} R$")
