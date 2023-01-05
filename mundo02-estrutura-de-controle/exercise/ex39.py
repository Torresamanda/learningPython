from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Você é homem ou mulher: ')).upper()

idade = atual - nasc
print('Você nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if sexo == 'HOMEM':
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE ')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado a {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Mulheres não precisam se alistar.')


