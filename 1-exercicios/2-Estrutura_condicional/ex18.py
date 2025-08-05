"""
Ex 18 - Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

def data_valida(data):
    try:
        dia, mes, ano = map(int, data.split('/'))
    except ValueError:
        return False  # Não conseguiu converter para inteiros ou formato errado

    if ano < 1:
        return False

    if mes < 1 or mes > 12:
        return False

    # Verifica o número máximo de dias no mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        max_dias = 31
    elif mes in [4, 6, 9, 11]:
        max_dias = 30
    elif mes == 2:
        # Verifica se ano é bissexto
        bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
        max_dias = 29 if bissexto else 28
    else:
        return False

    if dia < 1 or dia > max_dias:
        return False

    return True


data = input("Digite uma data no formato dd/mm/aaaa: ")

if data_valida(data):
    print(f"A data {data} é válida.")
else:
    print(f"A data {data} é inválida.")
