# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
b = n1 * n2
c = n1 / n2
d = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {} \ne a divisão é {:.3f}.'.format(a, b, c), end='')
print(' Divisão inteira {} \ne potência {}'.format(d , e))