n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7 and media <= 10:
    print('Você está aprovado! Sua média é {:.2f}!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você está em Recuperação! Sua média é {:.2f}'.format(media))
elif media < 5 and media >= 0:
    print('Você foi reprovado! Sua média é {:.2f}!'.format(media))
else:
    print('Notas inválidas, digite novamente uma nota entre 0 e 10!')