"""
Ex 19 - Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e 
unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades

12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input("Digite um número inteiro menor que 1000: "))

if num < 0 or num >= 1000:
    print("Número inválido! Deve ser entre 0 e 999.")
else:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = num % 10

    partes = []

    # Função para formar o texto correto de cada parte
    def texto_quantidade(valor, singular, plural):
        if valor == 1:
            return f"1 {singular}"
        elif valor > 1:
            return f"{valor} {plural}"
        else:
            return ""

    c = texto_quantidade(centenas, "centena", "centenas")
    d = texto_quantidade(dezenas, "dezena", "dezenas")
    u = texto_quantidade(unidades, "unidade", "unidades")

    # Adiciona partes não vazias na lista
    if c:
        partes.append(c)
    if d:
        partes.append(d)
    if u:
        partes.append(u)

    # Formata a saída com vírgulas e "e"
    if len(partes) == 1:
        resultado = partes[0]
    elif len(partes) == 2:
        resultado = f"{partes[0]} e {partes[1]}"
    else:
        resultado = ", ".join(partes[:-1]) + " e " + partes[-1]

    print(f"{num} = {resultado}")
