frase = str(input('Digite uma frase: ')).upper()
palavra = frase.split()
juntos = ''.join(palavra)
# inverso = ''
inverso = juntos[::-1]
# for letra in range(len(juntos) - 1, -1, -1):
#     inverso += juntos[letra]
print('O inverso de {} é {}'.format(juntos, inverso))
if inverso == juntos:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
