while True:
    num = int(input('Quer ver a tabuada de qual valor? ' ))
    print('-'*30)
    if num < 0:
        break

    for c in range(1, 11):
        print('{} X {:2} = {}'.format(num, c, num*c))
    print('-'*30)

print('Programa encerrado. Volte sempre!')