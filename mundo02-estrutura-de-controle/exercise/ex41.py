from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc

if idade <= 9: 
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade  <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 26:
    print('Classificação: MASTER')
else:
    print('Ano de nascimento incorreto, tente novamente!')