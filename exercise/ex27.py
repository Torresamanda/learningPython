nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print('Muito prazer em te conhecer! \nSeu primeiro nome é {}.'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))