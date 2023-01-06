somaidade = 0
mediaidade = 0
maiorIdadeHomem = 0
nomeVelhor = ''
totalMulher = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelhor = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelhor = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelhor))
print('Ao todo tem {} mulheres com menos de 20 anos'.format(totalMulher))