from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('Emapate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada Inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada Inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empatou')
    else:
        print('Jogada Inválida')
