pessoa = dict()
lista = list()

for c in range(0, 1):
    pessoa['nome'] = str(input('Nome: '))
    pessoa['media'] = float(input(f'Média de {pessoa["nome"]}: '))
    lista.append(pessoa.copy())

print(f'Nome é igual a {pessoa["nome"]}')
print(f'Média é igual a {pessoa["media"]}')

for p in lista:
    if pessoa["media"] >= 7:
        print(f'Situação é igual a Aprovado')
    elif 5 <= pessoa["media"] <= 7:
        print(f'Situação é igual a Recuperação')
    else:
        print(f'Situação igual a Reprovado')
        