num = int(input('Digite um número para ver sua tabuada: '))

for c in range(0, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))