dado = list()
pessoas = list()

maiorpeso = menorpeso = 0

while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))

    if len(pessoas) == 0:
        maiorpeso = menorpeso = dado[1]
    else:
        if dado[1] > maiorpeso:
            maiorpeso = dado[1]
        if dado[1] < menorpeso:
            menorpeso = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break

print(f'Existe um total de {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso foi de {menorpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end='')
print()